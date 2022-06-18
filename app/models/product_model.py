from app.integrations.db import db
from sqlalchemy import Integer, String, Float
from app.reusable.models import TimeStampModel


class Product(TimeStampModel):
    __tablename__ = "Product"
    product_id = db.Column(Integer, primary_key=True, autoincrement="auto", index=True)
    name = db.Column(String(200))
    code = db.Column(String(200))
    category = db.Column(String(200))
    price = db.Column(Float, default=0.0)
    quantity = db.Column(Integer, default=0)
    percentage_discount = db.Column(Float, default=0.0)

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        db.session.commit()
        db.session.flush()

    def save(self):
        db.session.add(self)
        db.session.commit()
        db.session.flush()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        db.session.flush()
