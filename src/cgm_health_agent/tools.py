from langchain.tools import tool

@tool
def detect_meal_spike(glucose_readings: list[float]) -> str:
    """
    Detect post-meal glucose spike pattern.
    """

    rise = glucose_readings[-1] - glucose_readings[0]

    if rise > 50:
        return "HIGH_MEAL_SPIKE"

    if rise > 30:
        return "MODERATE_MEAL_SPIKE"

    return "NO_MEAL_SPIKE"

@tool
def detect_trend(glucose_readings: list[float]) -> str:
    """
    Detect glucose trend.
    """
    
    diff = glucose_readings[-1] - glucose_readings[-3]

    if diff > 15:
        return "RISING"

    if diff < -15:
        return "FALLING"

    return "STABLE"

@tool
def assess_glucose_risk(glucose_readings: list[float]) -> str:
    """
    Assess glucose risk level.
    """

    latest = glucose_readings[-1]

    if latest < 70:
        return "HIGH"

    if latest > 180:
        return "HIGH"

    return "LOW"


@tool
def send_watch_notification(severity: str, message: str, action_cta: str):
    """
    Sends a notification to the watch with a specific haptic intensity.
    Severity: 'CRITICAL' (Low/Hypo), 'WARNING' (High/Spike), 'INFO' (Trend)
    """
    # Logic to send to the wearable UI
    return f"Sent {severity} alert to watch: {message} | Button: {action_cta}"