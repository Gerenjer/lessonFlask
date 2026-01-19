from flask import Blueprint, request, jsonify
from crud import (create_user, create_product, create_tag, create_color, add_color_to_product, add_tag_to_product, 
                  get_users, get_product, get_user_by_email, get_products)
from models import User, Product
from pydantic import BaseModel, validator
from pydantic.error_wrappers import ValidationError

api = Blueprint('api', __name__)

@api.route('/users', methods=['GET'])
def show_users():
    return jsonify(get_users())

@api.route('/users/<string:email>', methods=['GET']) # параметр пути - часть пути
def show_users(email):
    return jsonify(get_user_by_email(email))

@api.route('/product/<int:id>', methods=['GET'])
def show_product(id):
    return jsonify(get_product(id))

@api.route('/products', methods=['GET'])
def show_products():
    return jsonify(get_products())

@api.route('/users', methods=['POST'])
def register_user():
    user = create_user(**request.json)
    return jsonify({"id": user.id, 'email': user.email}), 201

@api.route('/products', methods=['POST'])
def add_product():
    data = rerquest.json
    product = create_product(
        name=data['name'],
        description=data.get('description', ''),
        price=float(data['price']),
        stock=int(data.get('stock', 0))
    )
    return jsonify({"id": product_id, "name": product.name}), 201

