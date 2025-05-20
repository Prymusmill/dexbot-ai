# run_worker.py

import time
import os
import json
from datetime import datetime
from config.settings import load_settings
from core.trade_executor import simulate_trade

STATE_FILE = "data/state.json"
MEMORY_FILE = "data/memory.csv"

def load_state():
    if not os.path.exists(STATE_FILE):
        return {"count": 0}
    with open(STATE_FILE, "r") as f:
        return json.load(f)

def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f)

def export_results():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    export_path = f"data/results_{timestamp}.csv"
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as src, open(export_path, "w") as dst:
            dst.write(src.read())
        print(f"✅ Eksportowano dane do: {export_path}")
    else:
        print("⚠️ Brak pliku memory.csv — eksport pominięty")

if __name__ == "__main__":
    print("🚀 Uruchamiam bota DEX przez GitHub Actions...")
    settings = load_settings()
    state = load_state()

    for i in range(5):  # 5 symulacji na uruchomienie
        print(f"🔁 Symulacja {state['count'] + 1}")
        simulate_trade(settings)
        state["count"] += 1
        time.sleep(1)

    save_state(state)

    if state["count"] % 100 == 0:
        export_results()