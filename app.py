from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "Bridge is Online!"

@app.route('/trade', methods=['POST'])
def trade():
    data = request.get_json()
    
    # Exness MT5 WebTerminal API Simulation
    # এখানে আপনার ট্রেডিং লজিক প্রসেস হবে
    login = data.get('login')
    password = data.get('password')
    server = data.get('server')
    symbol = data.get('symbol')
    action = data.get('action')
    volume = data.get('volume')

    # সাকসেস মেসেজ রিটার্ন করা
    return jsonify({
        "status": "success",
        "message": f"Trade {action} {volume} {symbol} placed successfully on {server}!"
    }), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
