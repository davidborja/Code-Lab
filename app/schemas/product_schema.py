from app.integrations.ma import ma

from app.models.product_model import Product


class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        load_instance = True
        load_only = ("Product",)
        exclude = ("created", "modified", "product_id")
