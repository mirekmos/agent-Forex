import streamlit as st
import requests

BASE_API = "http://localhost:5050"

def get_news():
    try:
        return requests.get(f"{BASE_API}/news").json()
    except Exception as e:
        return {"error": str(e)}

def get_sentiment(symbol):
    try:
        return requests.get(f"{BASE_API}/sentiment?symbol={symbol}").json()
    except Exception as e:
        return {"error": str(e)}

def get_calendar():
    try:
        return requests.get(f"{BASE_API}/calendar").json()
    except Exception as e:
        return {"error": str(e)}

st.title("Agent wywiadu Forex (Smyth Runtime lokalny)")

symbol = st.text_input("Podaj instrument (np. EURUSD, XAUUSD):", value="EURUSD")

if st.button("📰 Najnowsze wiadomości Forex"):
    st.write(get_news())

if st.button("📊 Sentyment rynkowy"):
    st.write(get_sentiment(symbol))

if st.button("📅 Kalendarz ekonomiczny"):
    st.write(get_calendar())

st.info("Dane pobierane z Twojego lokalnego agenta (localhost:5050). Konsola z agentem musi być otwarta!")

