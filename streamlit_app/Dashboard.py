# streamlit_app/Dashboard.py
import streamlit as st
import json
import os
import time
from performance import show_performance
from core.trade_executor import simulate_trade
from config.settings import load_settings

CONFIG_PATH = "config/settings.json"

def load_settings_local():
    try:
        with open(CONFIG_PATH, "r") as f:
            return json.load(f)
    except Exception as e:
        st.error(f"Nie udało się załadować ustawień: {e}")
        return {}

def main():
    st.set_page_config(page_title="DEXBot AI", layout="centered")
    st.title("🤖 DEXBot AI – Dashboard")

    settings = load_settings_local()
    if settings:
        st.subheader("🔧 Ustawienia bota")
        st.json(settings)

        st.subheader("📊 Stan bota")
        st.write("Tryb działania:", settings.get("mode", "brak"))
        st.write("Maks. transakcji/min:", settings.get("max_trades_per_minute", "n/d"))
        st.write("Wielkość transakcji (USD):", settings.get("trade_amount_usd", "n/d"))

        st.subheader("🚦 Status:")
        st.success("Bot działa w trybie symulacyjnym. Uczenie trwa...")

        # 🧪 PRZYCISKI START/STOP/RESET
        st.subheader("🧪 Sterowanie symulacją")

        if "running" not in st.session_state:
            st.session_state.running = False

        col1, col2, col3 = st.columns(3)

        with col1:
            if st.button("🟢 START (5 symulacji)"):
                st.session_state.running = True
                for i in range(5):
                    if not st.session_state.running:
                        break
                    simulate_trade(settings)
                    time.sleep(1)
                st.session_state.running = False
                st.success("Symulacja zakończona.")

        with col2:
            if st.button("⛔ STOP"):
                st.session_state.running = False
                st.warning("Zatrzymano.")

        with col3:
            if st.button("🧹 RESET pamięci"):
                try:
                    os.remove("data/memory.csv")
                    st.success("Pamięć wyczyszczona.")
                except:
                    st.info("Brak pliku do usunięcia.")

        # 📊 Wizualizacja skuteczności
        show_performance()

if __name__ == "__main__":
    main()