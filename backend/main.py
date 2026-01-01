from fastapi import FastAPI
from datetime import datetime

from network.scanner import scan_network, enrich_devices
from agents.reasoning_agent import run_security_agent

# -------------------------------------------------------------------
# FASTAPI APP INITIALIZATION
# -------------------------------------------------------------------

app = FastAPI(
    title="Agentic AI IoT Security System",
    description="Autonomous IoT network protection using LangChain agents",
    version="1.0.0"
)


# -------------------------------------------------------------------
# HEALTH CHECK
# -------------------------------------------------------------------
@app.get("/")
def health_check():
    """
    Health check endpoint
    """
    return {
        "status": "running",
        "service": "Agentic AI IoT Security System",
        "timestamp": datetime.utcnow().isoformat()
    }


# -------------------------------------------------------------------
# DEVICE DISCOVERY API
# -------------------------------------------------------------------
@app.get("/devices")
def discover_devices():
    """
    Discovers and returns all IoT devices on the network
    """
    devices = scan_network()
    enriched_devices = enrich_devices(devices)

    return {
        "timestamp": datetime.utcnow().isoformat(),
        "device_count": len(enriched_devices),
        "devices": enriched_devices
    }


# -------------------------------------------------------------------
# AGENTIC SECURITY API
# -------------------------------------------------------------------
@app.get("/protect")
def protect_network():
    """
    Triggers the LangChain-powered agentic security workflow.

    The agent:
    - Discovers devices
    - Detects anomalies
    - Reasons about risk
    - Takes autonomous actions
    - Explains decisions
    """
    result = run_security_agent()

    return {
        "timestamp": datetime.utcnow().isoformat(),
        "agent_response": result
    }
