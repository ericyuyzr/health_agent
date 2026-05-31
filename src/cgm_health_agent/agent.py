import os

from langchain_openai import ChatOpenAI

from langchain.agents import create_agent

from cgm_health_agent.prompt import SYSTEM_PROMPT
from cgm_health_agent.tools import (
    assess_glucose_risk,
    detect_trend,
    detect_meal_spike,
)
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory

BASE_URL = os.getenv(
    "OPENAI_API_BASE", "http://10.42.208.168:8083/mimik-ai/openai/v1"
)
API_KEY = os.getenv("OPENAI_API_KEY", "1234")

llm = ChatOpenAI(
    model="qwen3-1.7b",
    base_url=BASE_URL,
    api_key=API_KEY,
    temperature=0,
    timeout=300,
    max_retries=2,
)

tools = [
    detect_meal_spike,
    detect_trend,
    assess_glucose_risk,
]

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=SYSTEM_PROMPT,
)

# Simple in-memory session store for chat histories
_HISTORY_STORE: dict[str, InMemoryChatMessageHistory] = {}

def _get_session_history(session_id: str) -> InMemoryChatMessageHistory:
    if session_id not in _HISTORY_STORE:
        _HISTORY_STORE[session_id] = InMemoryChatMessageHistory()
    return _HISTORY_STORE[session_id]


agent_with_history = RunnableWithMessageHistory(
    agent,
    _get_session_history,
    input_messages_key="messages",
    history_messages_key="chat_history"
)

agent_executor = agent_with_history