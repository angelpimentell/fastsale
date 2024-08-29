from flask import Flask, request, jsonify
from flask_migrate import Migrate
from config import Config
from models import db, Product

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)


@app.route('/products', methods=['POST'])
def create_product():
    data = request.json
    name = data.get('name')
    price = data.get('price')

    if not name or not price:
        return jsonify({"error": "Incomplete data"}), 400

    new_product = Product(name=name, price=price)
    db.session.add(new_product)
    db.session.commit()

    return jsonify({"message": "Product created",
                    "product": {"id": new_product.id, "name": new_product.name, "price": new_product.price}}), 201


@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([{"id": product.id, "name": product.name, "price": product.price} for product in products])


if __name__ == '__main__':
    app.run(debug=True)
