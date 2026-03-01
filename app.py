from flask import Flask, request
import requests
import os

app = Flask(__name__)

@app.get('/')
def home():
    return "Bridge is Online!"

@app.route('/trade', methods=['POST'])
def trade():
    data = request.get_json()
    # এটি একটি পাবলিক গেটওয়ে যা আপনার হয়ে ট্রেডটি প্রসেস করবে
    external_url = "https://mt5-api-service.onrender.com/execute"
    try:
        response = requests.post(external_url, json=data, timeout=20)
        return response.text, response.status_code
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
