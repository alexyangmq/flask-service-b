from flask import Flask, jsonify
import requests

app = Flask(__name__)

items = [
    {
        'name': 'Table',
        'price': 5000
    },
    {
        'name': 'Chair',
        'price': 3000
    }
]


@app.route('/')
def index():
    return jsonify(message='Resting fine...')
#     return jsonify(message='Working fine...')
#     url = 'http://flask-service-a-lb-1769393057.us-east-1.elb.amazonaws.com/items'
#     response = requests.get(url)
#     return response.text

@app.route('/items')
def fetch_items():
    return jsonify(items=items)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
