import time
from core.trade_executor import simulate_trade
from config.settings import load_settings

def run_bot_loop():
    settings = load_settings()
    interval = 60 / settings.get("max_trades_per_minute", 1)

    while True:
        simulate_trade(settings)
        time.sleep(interval)

if __name__ == "__main__":
    run_bot_loop()
