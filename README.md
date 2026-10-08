# Red Bull Commercial Intelligence Agent

### Setup
[Instructions to install dependencies and run the app]
For Database, download the container via Podman since no macos version is available.

```bash
podman pull container-registry.oracle.com/database/free:latest
```

Install ollama for macos. Then pull and run. Using tinyllama due to memory constraints.



```bash
sudo curl -fsSL https://ollama.com/install.sh | sh
ollama pull tinyllama
ollama serve
```

See the directory michaels_settings. I have saved the configuration file from a previous test.

### How It Works
[Explain your architecture: how you load data, structure prompts, call the LLM, return results]


### Design Decisions
- **LLM choice**: [Why this one?]
- **Prompt strategy**: [How do you feed context? What's your system prompt?]
- **Error handling**: [What happens if the LLM fails?]
- **Trade-offs**: [What did you optimize for? What did you skip?]

### Sample Interaction