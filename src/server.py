from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain

class ChatbotServer:
    """Backend server managing data loading, embeddings, and LLM generation."""
    
    def __init__(self, csv_file_path: str, llm_model: str = "tinyllama"):
        self.csv_file_path = csv_file_path
        self.llm_model = llm_model
        self.rag_chain = None
        self._initialize_pipeline()

    def _initialize_pipeline(self):
        """Sets up the RAG pipeline components."""
        print(f"Loading data from {self.csv_file_path}...")
        loader = CSVLoader(file_path=self.csv_file_path)
        docs = loader.load()

        print("Initializing embeddings and vector database...")
        embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        vector_store = FAISS.from_documents(docs, embeddings)

        #defining
        retriever = vector_store.as_retriever(search_kwargs={"search_type": "similarity", "k": 5, "fetch_k": 20})

        print(f"Connecting to local model ({self.llm_model})...")
        llm = OllamaLLM(model=self.llm_model)

        system_prompt = (
            """You are a helpful financial assistant. Use the following pieces of retrieved context to answer a human with marketing profession. If you dont know the answer based on the context, just say you don't know. The answers should be concise.
            \n\n"""
            "Context:\n{context}"
        )
        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("human", "{input}"),
        ])

        question_answer_chain = create_stuff_documents_chain(llm, prompt)
        self.rag_chain = create_retrieval_chain(retriever, question_answer_chain)

    def query(self, user_input: str) -> str:
        """Processes a query through the RAG chain and returns the answer."""
        if not self.rag_chain:
            raise RuntimeError("RAG chain failed to initialize.")
        
        response = self.rag_chain.invoke({"input": user_input})
        return response.get("answer", "Error: No answer generated.")