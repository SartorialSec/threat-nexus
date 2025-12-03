from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import json

app = FastAPI(title="ThreatNexus API")

# Load Framework Logic
with open("framework_map.json", "r") as f:
    FRAMEWORK_MAP = json.load(f)

class Alert(BaseModel):
    source_ip: str
    event_type: str  # e.g., "phishing_email_detected"
    payload_hash: str | None = None

class ContextualizedThreat(BaseModel):
    alert: Alert
    kill_chain_phase: str
    mitre_id: str
    mitre_technique: str
    severity: str

@app.post("/ingest-alert", response_model=ContextualizedThreat)
async def ingest_alert(alert: Alert):
    """
    Ingests a raw alert and maps it to CKC and MITRE.
    """
    # Logic: Map raw event types to our framework dictionary
    # In a real app, this would be a database lookup or AI classifier
    
    mapping = {}
    
    if "scan" in alert.event_type:
        mapping = FRAMEWORK_MAP["reconnaissance"]
        technique = "T1595 (Active Scanning)"
    elif "phishing" in alert.event_type:
        mapping = FRAMEWORK_MAP["delivery"]
        technique = "T1566 (Phishing)"
    elif "shell" in alert.event_type:
        mapping = FRAMEWORK_MAP["exploitation"]
        technique = "T1059 (Command and Scripting Interpreter)"
    else:
        raise HTTPException(status_code=400, detail="Unknown Threat Type")

    return ContextualizedThreat(
        alert=alert,
        kill_chain_phase=mapping["kill_chain_phase"],
        mitre_id=mapping["mitre_tactic"],
        mitre_technique=technique,
        severity="HIGH" if mapping["kill_chain_phase"] == "Command and Control" else "MEDIUM"
    )
