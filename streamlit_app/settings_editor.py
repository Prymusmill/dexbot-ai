{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # streamlit_app/settings_editor.py\
import streamlit as st\
import json\
import os\
\
SETTINGS_PATH = "config/settings.json"\
\
def load_settings():\
    if os.path.exists(SETTINGS_PATH):\
        with open(SETTINGS_PATH, "r") as f:\
            return json.load(f)\
    return \{\}\
\
def save_settings(settings):\
    try:\
        with open(SETTINGS_PATH, "w") as f:\
            json.dump(settings, f, indent=2)\
        return True\
    except Exception as e:\
        st.error(f"Nie uda\uc0\u322 o si\u281  zapisa\u263  ustawie\u324 : \{e\}")\
        return False\
\
def settings_editor():\
    st.subheader("\uc0\u9881 \u65039  Edycja ustawie\u324  bota")\
\
    settings = load_settings()\
    if not settings:\
        st.warning("Nie uda\uc0\u322 o si\u281  wczyta\u263  konfiguracji.")\
        return\
\
    mode = st.selectbox("Tryb dzia\uc0\u322 ania", ["simulation", "real"], index=["simulation", "real"].index(settings.get("mode", "simulation")))\
    trade_amount = st.number_input("Kwota jednej transakcji (USD)", value=float(settings.get("trade_amount_usd", 0.01)), step=0.01)\
    max_trades = st.slider("Maks. transakcji na minut\uc0\u281 ", 1, 10, int(settings.get("max_trades_per_minute", 1)))\
    slippage = st.slider("Slippage (BPS)", 10, 100, int(settings.get("slippage_bps", 50)))\
    \
    if st.button("\uc0\u55357 \u56510  Zapisz ustawienia"):\
        settings["mode"] = mode\
        settings["trade_amount_usd"] = trade_amount\
        settings["max_trades_per_minute"] = max_trades\
        settings["slippage_bps"] = slippage\
\
        if save_settings(settings):\
            st.success("\uc0\u9989  Zapisano ustawienia.")\
        else:\
            st.error("\uc0\u10060  Nie uda\u322 o si\u281  zapisa\u263 .")}