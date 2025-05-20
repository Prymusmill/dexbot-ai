# run_worker.py
import time
from config.settings import load_settings
from core.trade_executor import simulate_trade

if __name__ == "__main__":
    print("🚀 Uruchamiam bota DEX w trybie ciągłym...")
    settings = load_settings()

    while True:
        simulate_trade(settings)
        time.sleep(60 / settings.get("max_trades_per_minute", 1))