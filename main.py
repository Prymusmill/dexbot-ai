import os
import streamlit.web.bootstrap
from streamlit_app.Dashboard import main as launch_dashboard

# Zmiana domyślnego portu na 8080 (dla Railway)
os.environ["PORT"] = "8080"

if __name__ == "__main__":
    streamlit.web.bootstrap.run(
        "streamlit_app/Dashboard.py",
        "",
        [],
        {}
    )