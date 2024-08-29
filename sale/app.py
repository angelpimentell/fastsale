from flask import Flask, render_template
import requests

app = Flask(__name__)

# URL de la API
API_URL = "http://localhost:5000/products"


@app.route('/')
def index():
    response = requests.get(API_URL)

    if response.status_code == 200:
        productos = response.json()

        lista_productos = []
        for producto in productos:
            nombre = producto.get('name')
            precio = producto.get('price')
            lista_productos.append({'name': nombre, 'price': precio})

        return render_template('index.html', productos=lista_productos)
    else:
        return "Error al obtener los productos", response.status_code


if __name__ == '__main__':
    app.run(debug=True, port=5001)
