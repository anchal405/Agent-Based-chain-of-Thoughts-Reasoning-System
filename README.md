# Multi-Agent Problem Solver with CrewAI & LangGraph

This project is a modular, multi-agent system for automated problem solving using [CrewAI](https://github.com/joaomdmoura/crewAI), [LangGraph](https://github.com/langchain-ai/langgraph), and large language models (LLMs) such as Gemini and Groq. It decomposes user queries, retrieves information, reasons about the problem, and composes a final answer—all in an automated, extensible workflow.

## Features
- **Agent-based architecture:** Specialized agents for problem decomposition, information retrieval, reasoning, and answer composition.
- **Flexible LLM support:** Easily switch between Gemini and Groq models.
- **Automated evaluation:** Built-in feedback and retry logic for improved answer quality.
- **CLI and graph-based workflows:** Interact via command line or as a LangGraph state machine.

## Directory Structure
```
magic 3/
├── agents.py         # Agent definitions (decomposer, retriever, reasoner, composer)
├── crew.py           # CLI entry point for running the agent crew
├── llm.py            # LLM selection and initialization (Gemini, Groq)
├── nodes.py          # LangGraph node functions (run, evaluate, finalize, retry)
├── state.py          # State definitions for LangGraph
├── tasks.py          # Task creation and dependency logic
├── tools.py          # (Reserved for custom tools, if any)
├── workflow.py       # LangGraph workflow and streaming CLI
├── requirements.txt  # Python dependencies
└── README.md         # Project documentation (this file)
```

## Setup
1. **Clone the repository**
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up environment variables:**
   - Create a `.env` file in the project root with your API keys:
     ```env
     GEMINI_API_KEY=your-gemini-api-key
     GROQ_API_KEY=your-groq-api-key
     ```

## Usage
### 1. CLI Crew Mode
Run the agent crew interactively:
```bash
python crew.py
```
- Enter your question when prompted.
- The system will decompose, retrieve, reason, and answer.

### 2. LangGraph Workflow Mode
Run the graph-based workflow with streaming updates:
```bash
python workflow.py
```
- Type your query at the prompt.
- The system will show step-by-step progress and results.
- Type `quit` or `exit` to leave.

## Agents & Tasks
- **Problem Decomposer:** Breaks down the main query into sub-problems.
- **Information Retriever:** Gathers facts from the web or knowledge base.
- **Reasoning Agent:** Combines facts and logic to address the problem.
- **Answer Composer:** Crafts the final answer in a concise, informative manner.

## Customization
- Add or modify agents in `agents.py`.
- Adjust task dependencies in `tasks.py`.
- Extend the workflow in `workflow.py` and `nodes.py`.

## Requirements
- Python 3.8+
- See `requirements.txt` for package list
- API keys for Gemini and/or Groq

---
*Inspired by CrewAI, LangGraph, and the power of modular AI workflows.*
