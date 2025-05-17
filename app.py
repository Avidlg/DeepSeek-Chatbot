from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

def chat_with_deepseek(prompt):
    url = "https://api.deepseek.com/v1/chat"
    headers = {"Content-Type": "application/json"}
    data = {"prompt": prompt}
    response = requests.post(url, json=data, headers=headers)
    return response.json().get("response", "Error: No response received")

@app.route('/')
def home():
    return render_template('index.html')  # Loads the UI

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    prompt = data.get("prompt")
    return jsonify({"response": chat_with_deepseek(prompt)})

if __name__ == '__main__':
    app.run(debug=True)
