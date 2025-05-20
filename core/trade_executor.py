from core.dex_client import get_quote
from learning.trainer import log_decision
import uuid

def simulate_trade(settings):
    print("[TradeExecutor] Symulacja transakcji...")

    input_mint = settings["input_token_mint"]
    output_mint = settings["output_token_mint"]
    amount = int(settings["trade_amount_usd"] * 1_000_000)  # 1 USDC = 1e6

    quote = get_quote(input_mint, output_mint, amount)
    if not quote:
        print("[TradeExecutor] Brak danych z Jupiter API.")
        return

    out_amount = quote.get("outAmount", "0")
    print(f"[TradeExecutor] Transakcja symulowana: {amount} → {out_amount}")

    # === Zapis do pamięci ===
    trade_id = str(uuid.uuid4())
    result = "success"
    context = {
        "amount_in": amount,
        "amount_out": out_amount,
        "input_token": input_mint,
        "output_token": output_mint
    }
    log_decision(trade_id, result, context)