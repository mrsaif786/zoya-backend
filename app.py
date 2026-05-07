from flask import Flask, request, jsonify, render_template
from datetime import datetime

app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Chat API
@app.route("/chat", methods=["POST"])
def chat():

    user_msg = request.json["message"].lower()

    # Greeting
    if "hello" in user_msg or "hi" in user_msg or "hii" in user_msg:
        reply = "Hello 👋 Main Zoya AI hoon. Kaise help kar sakti hoon?"

    # How are you
    elif "tum kaise ho" in user_msg:
        reply = "Main bilkul theek hoon 😊"

    # Name
    elif "tumhara naam" in user_msg or "naam kya hai" in user_msg:
        reply = "Mera naam Zoya AI hai 🤖"

    # Time
    elif "time" in user_msg:
        current_time = datetime.now().strftime("%H:%M:%S")
        reply = f"Abhi time hai ⏰ {current_time}"

    # Date
    elif "date" in user_msg:
        current_date = datetime.now().strftime("%d-%m-%Y")
        reply = f"Aaj ki date hai 📅 {current_date}"

    # Joke
    elif "joke" in user_msg:
        reply = "Programmer ne girlfriend kyu chhodi? Kyuki usme too many bugs the 😂"

    # India
    elif "india" in user_msg:
        reply = "India ek bahut sundar desh hai 🇮🇳"

    # Bye
    elif "bye" in user_msg:
        reply = "Goodbye 👋 Have a nice day!"

    # Thanks
    elif "thank" in user_msg:
        reply = "Welcome 😊"

    # Creator
    elif "creator" in user_msg or "kisne banaya" in user_msg:
        reply = "Mujhe Saif Ali ne banaya hai 😎"

    # AI
    elif "ai" in user_msg:
        reply = "Haan, main ek AI chatbot hoon 🤖"

    # Default
    else:
        reply = "Main abhi seekh rahi hoon 🤖"

    return jsonify({
        "reply": reply
    })


# Run Server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
