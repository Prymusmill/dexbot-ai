{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # streamlit_app/performance.py\
import streamlit as st\
import pandas as pd\
import os\
import matplotlib.pyplot as plt\
\
MEMORY_CSV = "data/memory.csv"\
\
def show_performance():\
    st.subheader("\uc0\u55357 \u56520  Skuteczno\u347 \u263  strategii")\
\
    if not os.path.exists(MEMORY_CSV):\
        st.info("Brak danych w pami\uc0\u281 ci bota. Uruchom najpierw kilka symulacji.")\
        return\
\
    df = pd.read_csv(MEMORY_CSV)\
    if df.empty:\
        st.info("Pami\uc0\u281 \u263  strategii jest pusta.")\
        return\
\
    success_count = df['result'].value_counts().get("success", 0)\
    fail_count = df['result'].value_counts().get("fail", 0)\
\
    st.markdown(f"\uc0\u9989  Sukces\'f3w: **\{success_count\}**")\
    st.markdown(f"\uc0\u10060  Pora\u380 ek: **\{fail_count\}**")\
\
    fig, ax = plt.subplots()\
    df['result'].value_counts().plot(kind='bar', ax=ax, color=["green", "red"])\
    ax.set_title("Rozk\uc0\u322 ad wynik\'f3w decyzji")\
    ax.set_ylabel("Liczba przypadk\'f3w")\
    st.pyplot(fig)}