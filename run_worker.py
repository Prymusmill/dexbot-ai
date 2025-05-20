# run_worker.py

import time
from config.settings import load_settings
from core.trade_executor import simulate_trade

if __name__ == "__main__":
    print("🚀 Uruchamiam bota DEX przez GitHub Actions...")
    settings = load_settings()

    for i in range(5):  # 5 transakcji na cykl
        print(f"🔁 Symulacja {i + 1}/5")
        simulate_trade(settings)
        time.sleep(1)  # można zwiększyć, np. do 10s