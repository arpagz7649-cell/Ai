from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

with open("words.txt", "r", encoding="utf-8") as f:
    DATABASE = set(
        word.strip().lower()
        for word in f
        if word.strip()
    )

current_letter = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/letter")
def letter():
    return {"letter": current_letter}

@app.route("/check", methods=["POST"])
def check():
    global current_letter

    word = request.json["word"].lower()

    if not word.startswith(current_letter.lower()):
        return {"valid": False, "message": "Huruf awal salah"}

    if word not in DATABASE:
        return {"valid": False, "message": "Kata tidak ada di database"}

    current_letter = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    return {
        "valid": True,
        "message": "Benar!",
        "nextLetter": current_letter
    }

if __name__ == "__main__":
    app.run(debug=True)
