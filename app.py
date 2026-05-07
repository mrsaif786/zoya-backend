from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "🔥 ZOYA AI RUNNING SUCCESSFULLY"

@app.route("/chat", methods=["POST"])
def chat():
    return {"reply": "Hello! Main Zoya AI hoon 🤖"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
