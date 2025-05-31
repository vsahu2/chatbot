from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_query = request.form['query'].lower()

    # Chatbot response
    bot_response = requests.post(
        'http://localhost:5000/chat',
        json={'message': user_query}
    ).json()

    # City data if city mentioned
    city_data = {}
    if "delhi" in user_query:
        city_data = requests.get('http://localhost:5001/city/delhi').json()
    elif "mumbai" in user_query:
        city_data = requests.get('http://localhost:5001/city/mumbai').json()

    return render_template('index.html', response=bot_response, city_data=city_data)

if __name__ == '__main__':
    app.run(port=5002)
