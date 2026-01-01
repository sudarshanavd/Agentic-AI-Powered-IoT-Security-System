from typing import Dict
from datetime import datetime
import random


# -------------------------------------------------------------------
# CONFIGURATION
# -------------------------------------------------------------------

BASELINE_TRAFFIC_RATE = 100     
ANOMALY_MULTIPLIER = 2.5        


# -------------------------------------------------------------------
# BASELINE SIMULATION (MVP)
# -------------------------------------------------------------------
def _get_current_traffic_rate() -> int:
    """
    Simulates current traffic rate for demo purposes.
    Replace this with real traffic metrics from Scapy later.
    """
    return random.randint(50, 300)


# -------------------------------------------------------------------
# ANOMALY DETECTION LOGIC
# -------------------------------------------------------------------
def detect_anomaly() -> Dict:
    """
    Detects anomalous behavior based on traffic deviation.

    Returns:
        Dict with anomaly flag, risk score, and explanation
    """

    current_rate = _get_current_traffic_rate()
    baseline = BASELINE_TRAFFIC_RATE

    deviation_ratio = current_rate / baseline

    anomaly_detected = deviation_ratio > ANOMALY_MULTIPLIER

    risk_score = min(deviation_ratio / 5.0, 1.0)

    return {
        "timestamp": datetime.utcnow().isoformat(),
        "baseline_rate": baseline,
        "current_rate": current_rate,
        "deviation_ratio": round(deviation_ratio, 2),
        "anomaly": anomaly_detected,
        "score": round(risk_score, 2),
        "explanation": (
            "Traffic spike detected beyond normal behavior"
            if anomaly_detected
            else "Traffic within expected range"
        )
    }
