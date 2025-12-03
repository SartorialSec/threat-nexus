import requests
import time
import random

API_URL = "http://localhost:8000/ingest-alert"

# Simulating an APT lifecycle (Cyber Kill Chain progression)
attack_sequence = [
    {"event_type": "port_scan_detected", "source_ip": "192.168.1.50"}, # Recon
    {"event_type": "phishing_email_detected", "source_ip": "10.0.0.5"}, # Delivery
    {"event_type": "powershell_execution", "source_ip": "10.0.0.5"},    # Exploitation
]

print("--- STARTING APT SIMULATION ---")

for attack in attack_sequence:
    print(f"Executing: {attack['event_type']}...")
    try:
        response = requests.post(API_URL, json=attack)
        data = response.json()
        print(f"  [+] Mapped to Kill Chain: {data['kill_chain_phase']}")
        print(f"  [+] Mapped to MITRE: {data['mitre_id']} -> {data['mitre_technique']}")
    except Exception as e:
        print(f"  [-] Error: {e}")
    
    time.sleep(2) # Pause between Kill Chain stages

print("--- SIMULATION COMPLETE ---")
