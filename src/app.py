from server import ChatbotServer
class ChatbotApp:
    """Frontend application managing the user interface loop."""
    
    def __init__(self, server: ChatbotServer):
        self.server = server

    def run(self):
        """Starts the chat interface loop."""
        print("\nReady! Chat with your CSV data (Type 'exit' to quit).")
        
        while True:
            try:
                user_input = input("\nYou: ").strip()
                
                if not user_input:
                    continue
                    
                if user_input.lower() in ['exit', 'quit']:
                    print("Goodbye!")
                    break

                # Send the query to the backend server
                answer = self.server.query(user_input)
                print(f"ollama: {answer}")
                
            except Exception as e:
                print(f"\nAn error occurred: {e}")