# wsgi.py
# pylint: disable=missing-docstring

from flask import Flask
app = Flask(__name__)

@app.route('/api/v1/products')
def products():
    PRODUCTS = {
    1: { 'id': 1, 'name': 'Skello' },
    2: { 'id': 2, 'name': 'Socialive.tv' },
    }
    return PRODUCTS
