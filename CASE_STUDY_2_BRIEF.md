# Red Bull Commercial Intelligence Agent

**Case Study 2 – Data Architect Interview**

---

## The Challenge

You work in Red Bull's commercial data team. Central Corporate Projects management is planning global commercial strategy, and Club leadership wants visibility into their own performance and how they compare to peers.

**Your stakeholders:**
- **Central Corporate Projects**: Need cross-club trends, performance rankings, and insights to inform investment decisions
- **Club Leadership**: Want to understand their own performance, identify what peers are doing well, and benchmark their strategies

**Your data** spans seven Red Bull sports clubs across regions and sports:
- **RBL** – Red Bull Leipzig (German football)
- **RBOA** – Red Bull Omiya Ardija (Japanese football)
- **RBNY** – Red Bull New York (MLS football)
- **EC** – EC Red Bull Salzburg (Austrian ice hockey)
- **EHC** – EHC Red Bull Munich (German ice hockey)
- **RBB** – Red Bull Bragantino (Brazilian football)
- **NRB** – Newcastle Red Bulls Rugby (Rugby)

Each club has 14 weeks of commercial data: ticket sales, merchandise revenue, and F&B performance. The data is clean but includes real-world narrative context—campaign launches, partnerships, market conditions—that explains the numbers.

**Your job: Build an LLM-powered application that lets stakeholders ask natural-language questions about club performance and get actionable insights.** Both corporate and club leadership should be able to explore the data without needing to write SQL or pivot tables.

---

## What You're Given

`red_bull_commercial_data.csv` — 294 rows, 7 clubs, 3 business domains, 14 weeks  
Columns: `club`, `week_of`, `domain`, `revenue_usd_k`, `units_sold`, `key_events`, `notes`

Example questions your agent should handle:
- "Which club is underperforming in merchandise and why?"
- "What patterns do you see in F&B sales across clubs?"
- "Compare ticket sales strategy: who's doing well and who should change approach?"
- "What's the relationship between key events and revenue spikes?"

---

## What You Build

A local application that:
1. Loads the CSV
2. Lets you ask natural-language questions about club performance
3. Uses an LLM agent to analyze, compare, and reason about the data
4. Returns insights (not just raw data)

---

## Requirements

- **No prescribed tech stack.** Use Python, Node, Go, Rust—whatever you're comfortable with.
- **Use free/open LLM options** (Ollama, LlamaCpp, Claude API free tier, Gemma, etc.).
- **Submit on GitHub** with code + README that explains setup, design decisions, and includes sample interactions.
- **Timeline**: You have a week, but it shouldn't take more than 4–8 hours of real work.

---

## Evaluation Rubric

We'll grade on:
- **Accuracy**: Does the agent answer questions correctly without hallucinating?
- **Interaction design**: Is the UX smooth? Can you ask natural questions?
- **Failure handling**: What happens when the LLM fails, the CSV is weird, or a question doesn't have an answer?
- **Code & architecture**: Is it readable, testable, maintainable?
- **Prompt engineering**: Did you think about how to feed context to the LLM?

---

## Submission

1. Create a GitHub repo with your code
2. Write a README explaining:
   - Setup & how to run it
   - Design decisions (why this LLM, how you structured prompts, etc.)
   - Sample interactions (paste actual Q&A showing the agent working)
   - Known limitations & what you'd do with more time
3. Send us the repo link, and share access to mark.atkins@redbull.com and patrik.rothenbuchner@redbull.com

---

## README Template

```markdown
# Red Bull Commercial Intelligence Agent

### Setup
[Instructions to install dependencies and run the app]

### How It Works
[Explain your architecture: how you load data, structure prompts, call the LLM, return results]

### Design Decisions
- **LLM choice**: [Why this one?]
- **Prompt strategy**: [How do you feed context? What's your system prompt?]
- **Error handling**: [What happens if the LLM fails?]
- **Trade-offs**: [What did you optimize for? What did you skip?]

### Sample Interaction
```
User: Which club has the best F&B performance?
Agent: Based on the data, RBNY has the highest average F&B revenue at $28.3k/week...

User: Why might that be?
Agent: Looking at the notes and events, RBNY has been running premium hospitality packages...
```

### Known Limitations
- [What doesn't work well?]
- [What would you fix with more time?]
- [Scale concerns?]

### Running Tests (if any)
[How to validate it works]
```

---

**This is real-world ambiguity.** You decide what's interesting, what to optimize for, and what "good" looks like. There are no gotchas—just build something you'd actually want to use.
