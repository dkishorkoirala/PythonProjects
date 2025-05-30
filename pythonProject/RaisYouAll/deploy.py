from flask import Flask, request, jsonify
from chatterbot import ChatBot

app = Flask(__name__)

raise_you_all = ChatBot('RaiseYouAll')

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = raise_you_all.get_response(user_input)
    return jsonify({"response": str(response)})

if __name__ == "__main__":
    app.run(debug=True)