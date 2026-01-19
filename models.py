from db_settings import db
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, Text, Float, Boolean, ForeignKey, Table

# m:m
product_tag = Table(
    'product_tag',
    db.metadata,
    Column('product_id', Integer, ForeignKey('product.id'), primary_key=True),
    Column('tg_id', Integer, ForeignKey("tag.id"), primary_key=True)
)

product_color = Table(
    'product_color',
    db.metadata,
    Column('product_id', Integer, ForeignKey('product.id'), primary_key=True),
    Column('color_id', Integer, ForeignKey('color.id'), primary_key=True)
)

class User(db.Model):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    is_active = Column(Boolean, default=True)

class Product(db.Model):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    description = Column(Text)
    price = Column(Float, nullable=False)
    stock = Column(Integer, default=0)

    tags = relationship('Tag', secondary=product_tag, back_populates='products')
    colors = relationship('Color', secondary=product_color, back_populates='products')

class Tag(db.Model):
    __tablename__ = 'tag'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    products = relationship("Product", secondary=product_tag, back_populates='tags')

class Color(db.Model):
    __tablename__ = 'color'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

    products = relationship("Product", secondary=product_color, back_populates='colors')
