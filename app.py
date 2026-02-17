from flask import Flask, jsonify, render_template

app = Flask(__name__)

PRODUCTS = [
    {"id": 1, "name": "Espresso", "price": 3.0, "description": "Strong and bold single shot."},
    {"id": 2, "name": "Cappuccino", "price": 4.5, "description": "Espresso with steamed milk foam."},
    {"id": 3, "name": "Latte", "price": 5.0, "description": "Smooth milk-forward coffee."},
    {"id": 4, "name": "Cold Brew", "price": 4.0, "description": "Slow-steeped and refreshing."},
]


@app.get("/")
def home():
    return render_template("index.html", products=PRODUCTS)


@app.get("/healthz")
def healthz():
    return jsonify({"status": "ok"}), 200


@app.get("/api/products")
def list_products():
    return jsonify(PRODUCTS), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
