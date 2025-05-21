import os
import streamlit.web.bootstrap
from streamlit_app.Dashboard import main as launch_dashboard

if __name__ == "__main__":
    os.environ["STREAMLIT_SERVER_PORT"] = os.getenv("PORT", "8501")  # <- użyj portu Railway lub 8501 domyślnie
    os.environ["STREAMLIT_SERVER_HEADLESS"] = "true"

    streamlit.web.bootstrap.run(
        launch_dashboard,  # <- to jest najważniejsza zmiana!
        "",
        [],
        {}
    )