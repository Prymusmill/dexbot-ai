import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import os

MEMORY_CSV = "data/memory.csv"

def show_performance():
    st.subheader("📊 Skuteczność strategii")

    if not os.path.exists(MEMORY_CSV):
        st.info("Brak danych w pamięci bota. Uruchom kilka symulacji.")
        return

    try:
        df = pd.read_csv(MEMORY_CSV)
    except Exception as e:
        st.error(f"Błąd ładowania danych: {e}")
        return

    if df.empty:
        st.info("Brak zapisanych decyzji do analizy.")
        return

    result_counts = df['result'].value_counts()

    # Wykres kołowy
    fig, ax = plt.subplots()
    ax.pie(result_counts, labels=result_counts.index, autopct="%1.1f%%", startangle=90)
    ax.axis("equal")
    st.pyplot(fig)

    # Liczby
    st.write("### 📌 Liczba decyzji:")
    st.write(result_counts)