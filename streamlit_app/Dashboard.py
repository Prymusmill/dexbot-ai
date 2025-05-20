# streamlit_app/Dashboard.py
import streamlit as st
import json
import os
from streamlit_app.performance import show_performance  # ← importujemy wcześniej

CONFIG_PATH = "config/settings.json"

def load_settings():
    try:
        with open(CONFIG_PATH, "r") as f:
            return json.load(f)
    except Exception as e:
        st.error(f"Nie udało się załadować ustawień: {e}")
        return {}

def main():
    st.set_page_config(page_title="DEXBot AI", layout="centered")
    st.title("🤖 DEXBot AI – Dashboard")
    
    settings = load_settings()
    if settings:
        st.subheader("🔧 Ustawienia bota")
        st.json(settings)

        st.subheader("📊 Stan bota")
        st.write("Tryb działania:", settings.get("mode", "brak"))
        st.write("Maks. transakcji/min:", settings.get("max_trades_per_minute", "n/d"))
        st.write("Wielkość transakcji (USD):", settings.get("trade_amount_usd", "n/d"))

        st.subheader("🚦 Status:")
        st.success("Bot działa w trybie symulacyjnym. Uczenie trwa...")

        # 📊 Wizualizacja skuteczności
        show_performance()

if __name__ == "__main__":
    main()