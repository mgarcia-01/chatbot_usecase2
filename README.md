# Red Bull Commercial Intelligence Agent

### Setup
[Instructions to install dependencies and run the app]

Install ollama for macos. Then pull and run. I am using tinyllama due to memory constraints. Change the version for different size models from ollama. 


```bash
sudo curl -fsSL https://ollama.com/install.sh | sh
ollama pull tinyllama
ollama serve
```

### How It Works
[Explain your architecture: how you load data, structure prompts, call the LLM, return results]

The core architecture consists of a application module, a server module, and a main module to run the entire application.

The root directory contains the requirements.txt and the run_app bash script to intiate podman (for MACOS), download models, run ollama, activate the python virtual environment, and run the chatbot application. 




### Design Decisions
- **LLM choice**: [Why this one?]
- **Prompt strategy**: [How do you feed context? What's your system prompt?]
- **Error handling**: [What happens if the LLM fails?]
- **Trade-offs**: [What did you optimize for? What did you skip?]

### Sample Interaction