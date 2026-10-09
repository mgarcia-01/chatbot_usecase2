from server import ChatbotServer
class ChatbotApp:
    """ Runs the terminal or user interface for the chatbot
    """
    
    def __init__(self, server: ChatbotServer):
        self.server = server

    def run(self):
        """Intiate the interface
        """
        
        print("\nWelcome to Red Bull Commercial Intelligence Agent!")    
        print("\nChat with your financial and commercial data (Type 'exit' to quit). CTRL + C works also")
        
        while True:
            try:
                user_input = input("\nUser Input: ").strip()
                
                if not user_input:
                    continue
                    
                if user_input.lower() in ['exit', 'quit']:
                    print("Hasta la vista!")
                    break

                # Send the query to the backend server
                answer = self.server.query(user_input)
                print(f"ollama: {answer}")
                
            except Exception as e:
                print(f"\n Encountered an error: {e}")