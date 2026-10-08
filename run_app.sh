CURWD="$PWD"
LOG_FILE="$CURWD/logs/run_aioptimizer.log"
exec > "$LOG_FILE" 2>&1
# Define the logging function
log_info() {
    echo "[INFO] $(date '+%Y-%m-%d %H:%M:%S') - $1" >> "$LOG_FILE"
}
. venv311/bin/activate
python -m pip install -r requirements.txt
# start podman 
podman machine start
curl -fsSL https://ollama.com/install.sh | sh
# this will only allow certain llama
ollama pull tinyllama
#ollama pull llama3.2
# Run the chatbot
#python src/reporting_chatbot.py
python src/run_chatbot.py
