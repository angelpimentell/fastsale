from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_migrate import Migrate
from config import Config
from models import db, Product

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)


@app.route('/products/create', methods=['GET', 'POST'])
def create_product():
    if request.method == 'POST':

        name = request.form['name']
        price = float(request.form['price'])

        if not name or not price:
            return jsonify({"error": "Incomplete data"}), 400

        new_product = Product(name=name, price=price)
        db.session.add(new_product)
        db.session.commit()

        return redirect('/')

    return render_template('create-product.html')


@app.route('/product/<int:product_id>')
def view_product(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('view_product.html', product=product)

@app.route('/products', methods=['GET'])
def read_products():
    products = Product.query.all()
    return jsonify([{"id": product.id, "name": product.name, "price": product.price} for product in products])


@app.route('/product/delete/<int:product_id>', methods=['GET'])
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)

    db.session.delete(product)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/', methods=['GET'])
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)


if __name__ == '__main__':
    app.run(debug=True)
