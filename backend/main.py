
from fastapi import FastAPI
from agents.reasoning_agent import run_security_agent
from network.scanner import scan_network

app = FastAPI()

@app.get("/devices")
def devices():
    return scan_network()

@app.get("/protect")
def protect():
    return run_security_agent()
