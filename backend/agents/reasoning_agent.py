from typing import Dict, Any
from datetime import datetime

from langchain.agents import Tool, initialize_agent
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory

# Import LangChain tools
from langchain_tools.tools import (
    discover_devices_tool,
    anomaly_detection_tool,
    firewall_block_tool,
    honeypot_deploy_tool
)


# -------------------------------------------------------------------
# AGENT INITIALIZATION
# -------------------------------------------------------------------
def _build_agent():
    """
    Builds and returns a LangChain agent configured for
    autonomous IoT security reasoning.
    """

    tools = [
        Tool(
            name="DiscoverDevices",
            func=discover_devices_tool,
            description=(
                "Discovers all devices connected to the home network. "
                "Use this to understand the current attack surface."
            ),
        ),
        Tool(
            name="DetectAnomaly",
            func=anomaly_detection_tool,
            description=(
                "Detects abnormal network behavior and returns a risk score "
                "between 0 and 1. Higher means more dangerous."
            ),
        ),
        Tool(
            name="BlockIP",
            func=firewall_block_tool,
            description=(
                "Blocks a malicious IP address at the firewall level. "
                "Use when risk score is high or attacker is confirmed."
            ),
        ),
        Tool(
            name="DeployHoneypot",
            func=honeypot_deploy_tool,
            description=(
                "Deploys a honeypot or honeytoken to trap and confirm attackers."
            ),
        ),
    ]

    llm = OpenAI(
        temperature=0,
        model_name="gpt-3.5-turbo"
    )

    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent="zero-shot-react-description",
        memory=memory,
        verbose=True
    )

    return agent


# -------------------------------------------------------------------
# MAIN AGENT EXECUTION
# -------------------------------------------------------------------
def run_security_agent() -> Dict[str, Any]:
    """
    Executes the agentic security workflow.

    Returns:
        Dict containing agent decisions and explanation
    """

    agent = _build_agent()

    system_prompt = """
You are an autonomous cybersecurity agent protecting a home IoT network.

Your responsibilities:
1. Discover devices on the network
2. Detect anomalous or malicious activity
3. Reason about risk using context
4. Decide whether defensive actions are required
5. Block malicious IPs if necessary
6. Deploy honeypots to confirm attacks
7. Explain your decisions clearly

Rules:
- Act autonomously without asking the user
- Minimize false positives
- Take decisive action if risk is high
- Always explain WHY you took an action
"""

    decision = agent.run(system_prompt)

    return {
        "timestamp": datetime.utcnow().isoformat(),
        "agent_type": "LangChain Agentic Security Brain",
        "decision_summary": decision
    }
