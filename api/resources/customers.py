from flask_restful import Resource, reqparse
from main import db
from database.models import CustomerModel

customer_args_parser = reqparse.RequestParser()
customer_args_parser.add_argument("customer_first_name", type=str, help="Name of customer (must be string)", required=True)
customer_args_parser.add_argument("customer_last_name", type=str, help="Last name of customer (must be string)")
customer_args_parser.add_argument("customer_email", type=str, help="Customer's email (must be string)")
customer_args_parser.add_argument("customer_phone", type=int, help="Customer's phone number (must be int)")
customer_args_parser.add_argument("customer_address", type=str, help="Customer's address (must be string)")

class CustomerResource(Resource):
    def get(self):
        return {"placeholder": "kupa"}

    def post(self):
        args = customer_args_parser.parse_args()
        customer = CustomerModel(
            first_name=args["customer_first_name"],
            last_name=args["customer_last_name"],
            email=args["customer_email"],
            phone=args["customer_phone"],
            address=args["customer_address"]
        )
        db.session.add(customer)
        db.session.commit()
        return args