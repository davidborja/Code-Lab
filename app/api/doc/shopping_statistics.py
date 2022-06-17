from flask_restx import Namespace, fields

shopping_statistics_ns = Namespace(
    "v1/shopping/statistics", description="EndPoint Service shoopping statistics"
)

shopping_statistics_response_200 = shopping_statistics_ns.model(
    "shoppingStatisticsSuccess", {"message": fields.String("message")}
)


shopping_statistics_response_400 = shopping_statistics_ns.model(
    "shoppingStatisticsError",
    {"message": fields.String("", description="Message", readonly=True)},
)


shopping_statistics_response_404 = shopping_statistics_ns.model(
    "shoppingStatisticsNotFound",
    {"message": fields.String("", description="Message", readonly=True)},
)
