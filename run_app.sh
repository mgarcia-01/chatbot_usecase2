CURWD="$PWD"
LOG_FILE="$CURWD/logs/run_aioptimizer.log"

mkdir -p "$CURWD/logs"

exec > >(tee "$LOG_FILE") 2>&1

log_info() {
    echo "[INFO] $(date '+%Y-%m-%d %H:%M:%S') - $1"
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
python src/app.py