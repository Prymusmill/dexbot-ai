# dexbot-ai

Projekt bota AI handlującego na DEX (np. Raydium na Solanie) z uczeniem maszynowym i panelem Streamlit.
Bot analizuje trendy rynkowe, podejmuje decyzje kup/sprzedaj/czekaj i uczy się na bieżąco.

## Główne funkcje:
- Symulacja handlu z zapamiętywaniem wyników
- Analiza skuteczności strategii
- Możliwość podpięcia rzeczywistego portfela Phantom
- Dashboard dostępny przez przeglądarkę (Streamlit Cloud)

## Struktura:
- `main.py` – uruchamia cały projekt
- `streamlit_app/` – pliki frontendowe
- `core/` – komunikacja z blockchain i portfelem
- `learning/` – logika uczenia i pamięć strategii
- `data/` – analiza świeczek i danych rynkowych
- `config/` – pliki konfiguracyjne

## Instrukcja uruchomienia:
1. Wgraj projekt do GitHub
2. Podłącz w Streamlit Cloud (plik główny: `streamlit_app/Dashboard.py`)
3. Skonfiguruj `settings.json` i `.env`