from db_settings import db 
from models import User, Product, Tag, Color

def create_user(email: str, password_hash: str):
    user = User(email=email, password_hash=password_hash)
    db.session.add(user)
    db.session.commit
    return user

def get_user_by_email(email: str):
    return User.query.filter_by(email=email).first()

def get_users():
    return User.query.all()


def create_product(name: str, description: str, price: float, stock: int = 0):
    product = Product(name=name, description=description, price=price, stock=stock)
    db.session.add(product)
    db.session.commit()
    return product

def get_product(id: int):
    return Product.query.get(id)

def get_products():
    return Product.query.all()

def create_tag(name: str):
    tag = Tag(name=name)
    db.session.add(tag)
    db.session.commit()
    return tag

def create_color(name: str):
    color = Color(name=name)
    db.session.add(color)
    db.session.commit()
    return color

def add_tag_to_product(product_id: int, tag_id: int):
    product = get_product(product_id)
    tag = Tag.query.get(tag_id)
    if product and tag: 
        product.tags.append(tag)
        db.session.commit()

def add_color_to_product(product_id: int, color_id: int):
    product = get_product(product_id)
    color = Color.query.get(color_id)
    if product and color:
        product.colors.append(color)
        db.session.commit()

def delete_user(user_id: int) -> bool:
    user = User.query.get(user_id)
    if not user:
        return False
    db.session.delete(user)
    db.session.commit()
    return True

def delete_product(product_id: int) -> bool:
    product = Product.query.get(product_id)
    if not product:
        return False
    db.session.delete(product)
    db.session.commit()
    return True

def delete_tag(tag_id: int) -> bool:
    tag = Tag.query.get(tag_id)
    if not tag:
        return False
    db.session.delete(tag)
    db.session.commit()
    return True

def delete_color(color_id: int) -> bool:
    color = Color.query.get(color_id)
    if not color:
        return False
    db.session.delete(color)
    db.session.commit()
    return True

