import json
import os

HISTORY_FILE = "chat_history.json"

def save_history(history):
    serialized_history = []
    for message in history:
        serialized_history.append({
            "role": message.role,
            "parts": [part.text for part in message.parts]
        })
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(serialized_history, f, ensure_ascii=False, indent=4)

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []