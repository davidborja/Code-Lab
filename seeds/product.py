from flask_seeder import Seeder, Faker, generator
from app.models.product_model import Product


class ProductSeeder(Seeder):

    # run() will be called by Flask-Seeder
    def run(self):
        print("----")
        # Create a new Faker and tell it how to create User objects
        faker = Faker(
            cls=Product,
            init={
                "name": generator.String("Product [a-z]{3}_[1-9]"),
                "code": generator.UUID(),
                "category": generator.String(
                    "(Personal hygiene|Office|Electronics|Food)"
                ),
                "price": generator.Integer(start=10, end=1000),
                "quantity": generator.Integer(start=10, end=100),
                "percentage_discount": generator.Integer(start=10, end=100),
            },
        )

        # Create 5 users
        for product in faker.create(50):
            print("Adding Product: %s" % product)
            self.db.session.add(product)
