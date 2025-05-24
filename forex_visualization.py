import streamlit as st
import requests

st.title("Forex Market Analyst - Wizualizacje")

# Wybór instrumentu
instrument = st.selectbox(
    "Wybierz instrument",
    ["EUR/USD", "GBP/USD", "USD/JPY", "GOLD", "BTC/USD"]
)

# Wybór typu danych do wizualizacji
data_type = st.selectbox(
    "Wybierz typ danych do wizualizacji",
    ["sentiment", "technical", "news", "social", "calendar", "cot", "all"]
)

# Przycisk do generowania wizualizacji
if st.button("Generuj wizualizację"):
    # TU WSTAW SWÓJ ADRES ENDPOINTU AGENTA Z CHMURY SmythOS
    agent_url = "https://TWOJ-AGENT-ID.agent.pa.smyth.ai/api/visualize_data"
    
    payload = {
        "instrument": instrument,
        "data_type": data_type
    }
    try:
        response = requests.post(agent_url, json=payload)
        if response.status_code == 200:
            res_json = response.json()
            visualization_html = res_json.get("visualization_html")
            if visualization_html:
                st.components.v1.html(visualization_html, height=800, scrolling=True)
            else:
                st.json(res_json)
                st.warning("Nie znaleziono kodu HTML wizualizacji, pokazano dane JSON.")
        else:
            st.error(f"Błąd HTTP {response.status_code}: {response.text}")
    except Exception as e:
        st.error(f"Wystąpił błąd: {str(e)}")
