{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # learning/strategy_memory.py\
import pandas as pd\
import os\
\
MEMORY_CSV = "data/memory.csv"\
\
def evaluate_memory():\
    if not os.path.exists(MEMORY_CSV):\
        print("[Memory] Brak danych do analizy.")\
        return\
\
    df = pd.read_csv(MEMORY_CSV)\
    success_rate = df['result'].value_counts(normalize=True).get("success", 0) * 100\
    print(f"[Memory] Skuteczno\uc0\u347 \u263  strategii: \{success_rate:.2f\}% na podstawie \{len(df)\} transakcji.")}