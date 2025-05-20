import json

SETTINGS_PATH = "config/settings.json"

def load_settings():
    try:
        with open(SETTINGS_PATH, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"[Settings] Błąd ładowania ustawień: {e}")
        return {}
