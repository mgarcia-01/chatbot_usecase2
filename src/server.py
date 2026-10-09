from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_huggingface import HuggingFaceEmbeddings as hfe
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate as cpt
from langchain.chains.combine_documents import create_stuff_documents_chain as csdc
from langchain.chains import create_retrieval_chain as crc

class chatbotServer:
    """Backend server managing data loading, embeddings, and LLM generation.
    """

    # TODO: modify the llm_model argument to accept a config or env variable in case a different model is selected
    def __init__(self, csv_file_path: str, llm_model: str = "tinyllama"):
        self.csv_file_path = csv_file_path
        self.llm_model = llm_model
        self.rag_chain = None
        self._initialize_pipeline()

    def _initialize_pipeline(self):
        """Sets up the RAG pipeline components. Using all minilm for sentence encoding 
        for semantic mapping. This is a private method for intializtion and loading of models 
        and financial data

        Parameters:
            loader (CSVLoader): Loads a csv file
            
            doc (list): list of documents loaded

            embeddings (HuggingFaceEmbeddings): sentence transformer defined and initalized

            vector_store (FAISS): vector store of the init embeddings and docs

            retriever (any): vector stores

            system_prompt (str): this defines the context of the input from the user.
        
        """
        print(f"Loading data from {self.csv_file_path}...")
        loader = CSVLoader(file_path=self.csv_file_path)
        doc = loader.load()

        #print("Initializing embeddings and vector database...")
        embeddings = hfe(model_name="all-MiniLM-L6-v2")
        # After initializing embeddings, we will get the vector stored after intializtion and add
        # the CSV file content to vector store
        vector_store = FAISS.from_documents(doc, embeddings)

        # defining retriever and setup for similarity search, return top k results.
        retriever = vector_store.as_retriever(search_kwargs={"search_type": "similarity", "k": 5, "fetch_k": 20})

        print(f" Connecting to model ...local llm... ({self.llm_model})...")
        llm = OllamaLLM(model=self.llm_model)

        # I setup my default system prompt. The system will use this for processing the semantic context of the input
        # TODO: setup this as an argument to provide the capability to define adhoc or via a config or env file.

        # TODO: Follow-up questions are not consistent
        system_prompt = (
            """You are a helpful and friendly assistant. Use the following pieces of retrieved context to answer an analyst with marketing profession. If you dont know the answer based on the context, just say you don't know. Keep the responses brief and concise and respond as a summary.
            \n\n"""
            "Context:\n{context}"
        )
        # Combine the input to the systems prompt for context

        # TODO: Check for issues from the system prompt
        prompt = cpt.from_messages([
            ("system", system_prompt),
            ("human", "{input}"),
        ])

        question_answer_chain = csdc(llm, prompt)
        self.rag_chain = crc(retriever, question_answer_chain)

    def query(self, user_input: str) -> str:
        """Processes a query through the RAG chain and returns the answer.

        Parameters:
            user_input (str):User query

        Returns:
            str:returns an answer
        """
        if not self.rag_chain:
            raise RuntimeError("RAG chain failed to initialize.")
        
        response = self.rag_chain.invoke({"input": user_input})
        return response.get("answer", "Error: No answer generated.")