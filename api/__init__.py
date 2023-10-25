from main import app, api
from resources.customers import CustomerResource

api.add_resource(CustomerResource, "/customer")

if __name__ == "__main__":
    app.run(debug=True)