import __init__
import app
import server


CSV_FILE = "./data/red_bull_commercial_data.csv"

# 1. Initialize the backend server
chatbot_server = server.ChatbotServer(csv_file_path=CSV_FILE)

# 2. Inject the server into the frontend app and run
app = app.ChatbotApp(server=chatbot_server)
app.run()