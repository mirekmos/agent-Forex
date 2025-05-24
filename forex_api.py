from flask import Flask, request, jsonify
from forex_dashboard import get_investing_news, get_forexfactory_calendar, get_dailyfx_sentiment

app = Flask(__name__)

@app.route("/news")
def news():
    return jsonify(get_investing_news())

@app.route("/calendar")
def calendar():
    return jsonify(get_forexfactory_calendar())

@app.route("/sentiment")
def sentiment():
    symbol = request.args.get("symbol", "EURUSD").upper()
    sent = get_dailyfx_sentiment()
    return jsonify({symbol: sent.get(symbol, "Brak danych")})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
