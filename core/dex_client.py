import requests

JUPITER_API_BASE = "https://quote-api.jup.ag/v6"

def get_quote(input_mint, output_mint, amount):
    url = f"{JUPITER_API_BASE}/quote"
    params = {
        "inputMint": input_mint,
        "outputMint": output_mint,
        "amount": int(amount),
        "slippageBps": 50
    }
    try:
        response = requests.get(url, params=params)
        return response.json()
    except Exception as e:
        print(f"[DEX Client] Błąd pobierania wyceny: {e}")
        return None
