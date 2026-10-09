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

Data is located via


### Design Decisions
- **LLM choice**: [Why this one?]
- **Prompt strategy**: [How do you feed context? What's your system prompt?]
- **Error handling**: [What happens if the LLM fails?]
- **Trade-offs**: [What did you optimize for? What did you skip?]

THe LLM of Choice was selected due to being a general purpose model. The specific version was selected due to the Macbook Air Limitations (Memory and Processing contraints), so a size of 700kb and 1b parameters seemed manageable without utilizing the entire system memory and failing upon submitting the prompt. It also provided short yet accurate answers based on the example prompts.

Context is fed using Langchain. The application utlizes langchaing_core prompts method to intake the user prompts. 

### Sample Interaction