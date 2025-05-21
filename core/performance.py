import pandas as pd
import streamlit as st

def show_performance():
    try:
        df = pd.read_csv("data/memory.csv")
        st.subheader("Podgląd danych z memory.csv")
        st.dataframe(df.tail(100))  # pokazuje ostatnie 100 wpisów
    except FileNotFoundError:
        st.warning("Plik memory.csv nie został znaleziony.")
    except Exception as e:
        st.error(f"Wystąpił błąd: {e}")