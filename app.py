from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():

    user_msg = request.json["message"].lower()

    if "hello" in user_msg:
        reply = "Hello! Main Zoya AI hoon 🤖"

    elif "tum kaise ho" in user_msg:
        reply = "Main theek hoon 😊"

    else:
        reply = "Mujhe aur train karo 🤖"

    return jsonify({
        "reply": reply
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
