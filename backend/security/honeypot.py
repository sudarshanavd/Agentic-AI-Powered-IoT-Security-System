from typing import Dict
from datetime import datetime
import socket
import threading


# -------------------------------------------------------------------
# CONFIGURATION
# -------------------------------------------------------------------

HONEYPOT_PORT = 2222
HONEYPOT_BANNER = b"Fake IoT Admin Interface\nLogin:"


# -------------------------------------------------------------------
# SIMPLE TCP HONEYPOT
# -------------------------------------------------------------------
def _honeypot_server():
    """
    Runs a lightweight fake service to attract attackers.
    """

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", HONEYPOT_PORT))
    server.listen(5)

    while True:
        client, addr = server.accept()

        try:
            client.send(HONEYPOT_BANNER)
            client.recv(1024)
            client.close()
        except Exception:
            pass


# -------------------------------------------------------------------
# DEPLOY HONEYPOT
# -------------------------------------------------------------------
def deploy_honeypot() -> Dict:
    """
    Deploys a fake IoT service honeypot.

    Returns:
        Dict with deployment status
    """

    timestamp = datetime.utcnow().isoformat()

    thread = threading.Thread(
        target=_honeypot_server,
        daemon=True
    )
    thread.start()

    return {
        "timestamp": timestamp,
        "action": "deploy_honeypot",
        "type": "fake_iot_admin_service",
        "port": HONEYPOT_PORT,
        "status": "active",
        "message": "Honeypot deployed and listening for attackers"
    }
