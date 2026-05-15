from flask import Flask, request, send_from_directory, jsonify
from flask_cors import CORS
from ai import OpenAICall
app = Flask(__name__)
CORS(app)

@app.route("/")
def serve_html():
    return send_from_directory('.', "index.html")

@app.route("/style.css")
def serve_css():
    return send_from_directory('.', "style.css")

@app.route("/index.js")
def serve_js():
    return send_from_directory('.', "index.js")

@app.route("/assets/loader.gif")
def serve_loader():
    return send_from_directory('.', "assets/loader.gif")

@app.route('/api/ai-prompt', methods=['POST'])
def handle_message():
    data = request.get_json()
    message = data.get('message')
    history = data.get('history')
    aiResponse = OpenAICall(message, history)
    aiText = aiResponse.choices[0].message.content
    return jsonify({'reply': aiText})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
