# Red Bull Commercial Intelligence Agent

### Setup
[Instructions to install dependencies and run the app]

Install ollama for macos. Then pull and run. I am using tinyllama due to memory constraints. Change the version for different size models from ollama. 

```bash
sudo curl -fsSL https://ollama.com/install.sh | sh
ollama pull tinyllama
ollama serve
```

The root directory contains the requirements.txt and the run_app.sh script to intiate podman (for MACOS), download models, run ollama, activate the python virtual environment, and run the chatbot application.

### How It Works

The core architecture consists of a application module, a server module, and a main module to run the entire application.

The root directory contains the requirements.txt and the run_app bash script to intiate podman (for MACOS), download models, run ollama, activate the python virtual environment, and run the chatbot application.

Project Structure
├── data
│   └── red_bull_commercial_data.csv
├── logs
│   └── run_aioptimizer.log
├── src
│   ├── app.py
│   └── server.py
├── tests
├── .gitignore
├── CASE_STUDY_2_BRIEF.md
├── LICENSE
├── README.md
├── requirements.txt
└── run_app.sh



### Design Decisions
- **LLM choice**: [Why this one?]
- **Prompt strategy**: [How do you feed context? What's your system prompt?]
- **Error handling**: [What happens if the LLM fails?]
- **Trade-offs**: [What did you optimize for? What did you skip?]

THe LLM of Choice was selected due to being a general purpose model. The specific version was selected due to the Macbook Air Limitations (Memory and Processing contraints), so a size of 700kb and 1b parameters seemed manageable without utilizing the entire system memory and failing upon submitting the prompt. It also provided short yet accurate answers based on the example prompts.

Context is fed using Langchain. The application utlizes langchaing_core prompts method to intake the user prompts. 
System prompt is 

```
You are a helpful financial assistant. Use the following pieces of retrieved context to answer a human with marketing profession. If you dont know the answer based on the context, just say you don't know
```

When it fails it will say it doesn't know. Or it will fail and say no answer is given. Or it will give the standard system error. So far the tests have given that it doesn't know.

I optimized for code readability, prepackaged model integrations and deployments (langchaing package), and for the hardware this was developed on (Macbook Air 16gb ram and m4 core - basic hardware). tinyllama was used due to the number of parameters, general usage, and it is only 700-800 kb.

Given more time and resources, I would perform deeper performance tests and larger scale models. I would also create a browser based user interface for better user experience. 

### Sample Interaction
The setup also creates a log directory and will log the stdout including the interactions. 

Q1
```
Q: Which club is underperforming in merchandise and why?
A: Pop-up store event exceeded expectation in new designer collaboration, but underperforming in merchandise.
```

Q2
```
Q: What patterns do you see in F&B sales across clubs?
A: Clubs with higher supply chain disruptions (i.e., those affected by supply chain disruptions), such as RBB and RBL, saw a significant decrease in sales due to Premium lounge bookings. On the other hand, clubs with less supply chain disruption, such as NRB, saw an increase in sales due to corporate events. Supply chain disruptions affected F&B margins due to decreased demand and increased prices.
```
Q3
```
Q: Compare ticket sales strategy: who's doing well and who should change approach?
A: Based on the context, EC's low attendance during the regular match day may be attributed to their lower revenues due to partial stadium access. It's recommended that EC change their approach to dynamic pricing strategies to match the high demand during the lower-attendance matches.
```

Q4
```
Q: What's the relationship between key events and revenue spikes?
A: Key Events: Online store surgery
Notes: E-commercce traffic increased 35% YoY
```