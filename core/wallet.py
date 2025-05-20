{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # core/wallet.py\
def get_wallet_balance(wallet_address):\
    # Wersja uproszczona (tylko komunikat testowy)\
    print(f"[Wallet] Sprawdzanie salda dla portfela: \{wallet_address\}")\
    return \{"SOL": 2.45, "USDC": 13.00\}  # Symulowane dane}