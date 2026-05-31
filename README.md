# health_agent

This project implements an AI-powered agent that analyzes Continuous Glucose Monitoring (CGM) readings and generates natural-language insights from the provided data.

The solution is built in Python using a modular src-based project structure and supports conversational interactions through an LLM-powered agent workflow.

**Quick Start**

- Install dependencies and sync environment (recommended using uv):: `uv sync`
- Configure endpoint (optional):
	- `set OPENAI_API_BASE=http://<host>/mimik-ai/openai/v1`
	- `set OPENAI_API_KEY=your_api_key`
- Run the example: `uv run main.py`

**What it contains**

- **Agent**: `src/cgm_health_agent/agent.py` — agent + `RunnableWithMessageHistory` wrapper
- **Prompt**: `src/cgm_health_agent/prompt.py` — system prompt template
- **Tools**: `src/cgm_health_agent/tools.py` — detection & assessment utilities
- **Test**: `src/test_connection.py` — lightweight endpoint connectivity check

**Usage (example)**

Invoke the agent with a session id to persist chat history:

```py
from cgm_health_agent.agent import agent_executor
from langchain_core.messages import HumanMessage

agent_executor.invoke(
		{"messages": [HumanMessage(content="Hello")]},
		config={"configurable": {"session_id": "default"}},
)
```

**Future Improvements**

- Add support for additional health metrics
- Add prediction models as tools
- Add action tools
- Further optimize prompts and response generation to improve clarity, consistency, and user experience


**Technologies Used**

- Python
- LangGraph / LangChain
- OpenAI API
- UV

