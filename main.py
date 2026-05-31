from cgm_health_agent.agent import agent_executor
from langchain_core.messages import HumanMessage
from cgm_health_agent.utils import extract_concise


def main():
    glucose_readings = [
        92,
        95,
        101,
        110,
        128,
        142
    ]

    query = f"""
    Analyze the following CGM readings:

    {glucose_readings}
    """

    response = agent_executor.invoke(
        {
            "messages": [HumanMessage(content=query)]
        },
        config={"configurable": {"session_id": "default"}},
    )

    # Post-process the model output into a short, useful string
    concise = extract_concise(response)
    print(concise)


if __name__ == "__main__":
    main()
