import pandas as pd
import os

MEMORY_CSV = "data/memory.csv"

def log_decision(trade_id, result, context):
    os.makedirs("data", exist_ok=True)
    row = {
        "id": trade_id,
        "result": result,
        "context": context
    }
    try:
        df = pd.DataFrame([row])
        if os.path.exists(MEMORY_CSV):
            df.to_csv(MEMORY_CSV, mode="a", header=False, index=False)
        else:
            df.to_csv(MEMORY_CSV, index=False)
        print(f"[Trainer] Zapisano decyzję: {row}")
    except Exception as e:
        print(f"[Trainer] Błąd zapisu do pamięci: {e}")
