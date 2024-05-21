from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Sample product data
products = [
    {
        'id': 1,
        'name': 'LED Light Bulb',
        'price': 9.99,
        'image': 'led-bulb.jpg',
        'category': 'Washing Machines'  # Corrected category
    },
    {
        'id': 2,
        'name': 'Power Strip',
        'price': 14.99,
        'image': 'power-strip.jpg',
        'category': 'Washing Machines'  # Corrected category
    },
    {
        'id': 3,
        'name': 'Extension Cord',
        'price': 7.99,
        'image': 'extension-cord.jpg',
        'category': 'Washing Machines'  # Corrected category
    },
    {
        'id': 4,
        'name': 'Smart Plug',
        'price': 19.99,
        'image': 'smart-plug.jpg',
        'category': 'Fridges'  # Corrected category
    },
    {
        'id': 5,
        'name': 'Surge Protector',
        'price': 24.99,
        'image': 'surge-protector.jpg',
        'category': 'Fridges'  # Corrected category
    },
    {
        'id': 6,
        'name': 'Electrical Tape',
        'price': 3.99,
        'image': 'electrical-tape.jpg',
        'category': 'Fridges'  # Added category
    },
    {
        'id': 7,
        'name': 'Cable Ties',
        'price': 5.99,
        'image': 'cable-ties.jpg',
        'category': 'Ovens'  # Added category
    },
    {
        'id': 8,
        'name': 'Circuit Breaker',
        'price': 39.99,
        'image': 'circuit-breaker.jpg',
        'category': 'Ovens'  # Added category
    }
]

# Group products by category
product_categories = {}
for product in products:
    category = product['category']
    if category not in product_categories:
        product_categories[category] = []
    product_categories[category].append(product)

@app.route('/')
def index():
    return render_template('index.html', product_categories=product_categories)

@app.route('/product/<int:product_id>', methods=['GET', 'POST'])
def product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product is None:
        return 'Product not found', 404

    if request.method == 'POST':
        # Handle WhatsApp message sending logic here
        print(f"Received order for product: {product['name']}")
        # You can add code to send a WhatsApp message here

    return render_template('product.html', product=product)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
