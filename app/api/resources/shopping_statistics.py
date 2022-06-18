from flask_restx import Resource
from flask import request
from marshmallow import ValidationError
from app.models.product_model import Product

from app.api.doc.shopping_statistics import (
    shopping_statistics_ns,
    shopping_statistics_response_200,
    shopping_statistics_response_400,
    shopping_statistics_response_404,
)
from app.schemas.product_schema import ProductSchema
from app.validations.validation_shopping_statistics import ValidationShoppingSchema


class ShoppingStatistics(Resource):
    product_schema = ProductSchema(many=True)
    validation_shopping = ValidationShoppingSchema()

    @shopping_statistics_ns.doc(
        model=shopping_statistics_response_200,
        params={
            "category": {
                "description": "product category",
                "type": "string",
                "required": False,
            }
        },
    )
    @shopping_statistics_ns.response(200, "Ok", shopping_statistics_response_200)
    @shopping_statistics_ns.response(
        404, "category not found", shopping_statistics_response_404
    )
    @shopping_statistics_ns.response(
        400, "bad request", shopping_statistics_response_400
    )
    def get(self):
        try:
            json = request.args
            json_data = self.validation_shopping.load(json)
            if "category" in json_data:
                products = Product.get_products_by_category(json_data["category"])
                categories = [(json_data["category"],)]
            else:
                products = Product.query.all()
                categories = Product.get_categories()

            products_schema = self.product_schema.dump(products)
            shopping_statistics = {}

            for category in categories:
                shopping_statistics[category[0]] = 0
                for product_schema in products_schema:
                    if category[0] == product_schema["category"]:
                        discount_price = 100.0 - product_schema["percentage_discount"]
                        price_product = product_schema["price"] * discount_price
                        total_price = product_schema["quantity"] * price_product
                        shopping_statistics[category[0]] = (
                            shopping_statistics[category[0]] + total_price
                        )

            data = {"data": shopping_statistics}

            return data, 200
        except ValidationError as instance:
            exception = instance.args[0]
            data = {"data": exception}
            return data, 400
        except Exception as instance:
            data = {"data": instance.args[0]}
            return data, 500
