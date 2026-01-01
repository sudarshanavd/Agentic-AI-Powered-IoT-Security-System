
from langchain.agents import Tool, initialize_agent
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory

from langchain_tools.tools import anomaly_tool, firewall_tool, honeypot_tool

def run_security_agent():
    tools = [
        Tool(
            name="DetectAnomaly",
            func=lambda _: anomaly_tool(),
            description="Detects network anomaly and returns risk score"
        ),
        Tool(
            name="BlockIP",
            func=lambda ip: firewall_tool("192.168.1.100"),
            description="Blocks a malicious IP using firewall"
        ),
        Tool(
            name="DeployHoneypot",
            func=lambda _: honeypot_tool(),
            description="Deploys a honeypot to trap attacker"
        )
    ]

    llm = OpenAI(temperature=0)
    memory = ConversationBufferMemory()

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent="zero-shot-react-description",
        memory=memory,
        verbose=True
    )

    result = agent.run(
        "Analyze the home network, detect threats, and take protective actions if required."
    )

    return {
        "agent_decision": result
    }
