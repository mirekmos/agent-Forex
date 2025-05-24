import streamlit as st
import requests

# === KONFIGURACJA: wstaw swój prawdziwy adres agenta SmythOS! ===
BASE_URL = "https://TWOJ_AGENT_ID.agent.pa.smyth.ai/api"

# --- Funkcje pomocnicze ---
def post_api(endpoint, payload):
    try:
        url = f"{BASE_URL}/{endpoint}"
        response = requests.post(url, json=payload, timeout=30)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Błąd HTTP {response.status_code}: {response.text}"}
    except Exception as e:
        return {"error": str(e)}

# --- Interfejs Streamlit ---
st.set_page_config(page_title="Agent wywiadu Forex", page_icon="💹")
st.title("Agent wywiadu Forex (SmythOS API)")

instrument = st.text_input("Podaj instrument (np. EURUSD, XAUUSD, GBPUSD, BTCUSD):", value="EURUSD")

st.subheader("Wybierz typ analizy lub wizualizacji")

option = st.selectbox(
    "Rodzaj zapytania:",
    [
        "Najnowsze wiadomości Forex",
        "Sentyment rynkowy",
        "Analiza techniczna",
        "Sentyment społecznościowy",
        "Pełna analiza rynkowa",
        "Wiadomości z lokalnego API",
        "Sentyment z lokalnego API",
        "Kalendarz ekonomiczny z lokalnego API",
        "Pełna analiza z lokalnego API",
        "Wizualizacja danych (HTML)"
    ]
)

if st.button("Wyślij zapytanie"):
    if option == "Najnowsze wiadomości Forex":
        res = post_api("forex_news", {"instrument": instrument})
        st.json(res)
    elif option == "Sentyment rynkowy":
        res = post_api("market_sentiment", {"instrument": instrument})
        st.json(res)
    elif option == "Analiza techniczna":
        res = post_api("technical_analysis", {"instrument": instrument})
        st.json(res)
    elif option == "Sentyment społecznościowy":
        res = post_api("social_sentiment", {"instrument": instrument})
        st.json(res)
    elif option == "Pełna analiza rynkowa":
        res = post_api("full_analysis", {"instrument": instrument})
        st.json(res)
    elif option == "Wiadomości z lokalnego API":
        res = post_api("api_news", {"instrument": instrument})
        st.json(res)
    elif option == "Sentyment z lokalnego API":
        res = post_api("api_sentiment", {"instrument": instrument})
        st.json(res)
    elif option == "Kalendarz ekonomiczny z lokalnego API":
        res = post_api("api_calendar", {"instrument": instrument})
        st.json(res)
    elif option == "Pełna analiza z lokalnego API":
        res = post_api("full_api_analysis", {"instrument": instrument})
        st.json(res)
    elif option == "Wizualizacja danych (HTML)":
        data_type = st.selectbox(
            "Wybierz rodzaj wizualizacji",
            ["sentiment", "technical", "news", "social", "calendar", "cot", "all"]
        )
        payload = {"instrument": instrument, "data_type": data_type}
        res = post_api("visualize_data", payload)
        if "visualization_html" in res:
            st.components.v1.html(res["visualization_html"], height=800, scrolling=True)
        else:
            st.json(res)

st.info("Dane pobierane są z Twojego agenta SmythOS (chmura). Wprowadź poprawny adres agenta w zmiennej BASE_URL.")
