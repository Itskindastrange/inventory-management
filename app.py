from flask import Flask, request, jsonify, render_template
from db.db import create_product, get_product, update_stock, create_invoice

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_product', methods=['POST'])
def add_product():
    data = request.form
    try:
        create_product(
            data['product_id'],
            data['name'],
            data['category'],
            float(data['price']),
            data['description']
        )
        return jsonify({"message": "Product added successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/get_product/<product_id>', methods=['GET'])
def get_product_by_id(product_id):
    product = get_product(product_id)
    if product:
        return jsonify(product), 200
    else:
        return jsonify({"error": "Product not found"}), 404

@app.route('/update_stock', methods=['POST'])
def update_stock_info():
    data = request.form
    try:
        update_stock(
            data['product_id'],
            int(data['quantity']),
            data['location']
        )
        return jsonify({"message": "Stock updated successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/create_invoice', methods=['POST'])
def create_invoice_info():
    data = request.form
    try:
        create_invoice(
            data['invoice_id'],
            data['date'],
            data['items']
        )
        return jsonify({"message": "Invoice created successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
