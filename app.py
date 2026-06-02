from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

angka_rahasia = random.randint(1, 100)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/tebak", methods=["POST"])
def tebak():
    global angka_rahasia

    data = request.json
    tebakan = int(data["angka"])

    if tebakan < angka_rahasia:
        return jsonify({"hasil": "Terlalu kecil!"})

    elif tebakan > angka_rahasia:
        return jsonify({"hasil": "Terlalu besar!"})

    else:
        angka_rahasia = random.randint(1, 100)
        return jsonify({"hasil": "Benar! Angka baru telah dibuat."})

if __name__ == "__main__":
    app.run(debug=True)
