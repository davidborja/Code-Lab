from flask_restx import Resource
from flask import request

# from flask import request, jsonify, make_response
# from marshmallow import ValidationError

from app.api.doc.shopping_statistics import (
    shopping_statistics_ns,
    shopping_statistics_response_200,
    shopping_statistics_response_400,
    shopping_statistics_response_404,
)


class ShoppingStatistics(Resource):
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
        json = request.args
        print(">>>", json)
        return json, 200
