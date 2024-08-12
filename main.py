from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)


@app.route('/fetch_data', methods=['GET'])
def fetch_data():
    api_url = 'http://127.0.0.1:7551/api/users'
    try:
        response = requests.get(api_url)
        response.raise_for_status()

        data = response.json()
        print("Data==================>", data)
        processed_data = process_data(data)

        return jsonify(processed_data)
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500


def process_data(data):
    for item in data:
        if 'first_name' or 'last_name' in item:
            item['first_name'] = item['first_name'].upper()
            item['last_name'] = item['last_name'].upper()

    return data


if __name__ == "__main__":
    app.run(debug=True)
