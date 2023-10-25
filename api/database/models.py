from main import db

class CustomerModel(db.Model):
    __tablename__ = 'Customers'
    CustomerID = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(50), index=True)
    LastName = db.Column(db.String(50))
    Email = db.Column(db.String(100))
    Phone = db.Column(db.String(20))
    Address = db.Column(db.String(255))
    order_details = db.relationship('OrderDetailsModel', back_populates='customer')

    def __init__(self, first_name, last_name, email, phone, address):
        self.FirstName = first_name
        self.LastName = last_name
        self.Email = email
        self.Phone = phone
        self.Address = address

class ProductModel(db.Model):
    __tablename__ = 'Products'

    ProductID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100))
    Description = db.Column(db.Text)
    Price = db.Column(db.Float)
    QuantityInStock = db.Column(db.Integer)
    order_items = db.relationship('OrderItemsModel', back_populates='product')

class OrderItemsModel(db.Model):
    __tablename__ = 'OrderItems'

    OrderItemID = db.Column(db.Integer, primary_key=True)
    ProductID = db.Column(db.Integer, db.ForeignKey('Products.ProductID'))
    Quantity = db.Column(db.Integer)
    OrderDetailID = db.Column(db.Integer, db.ForeignKey('OrderDetails.OrderDetailID'))
    product = db.relationship('ProductModel', back_populates='order_items')
    order_detail = db.relationship('OrderDetailsModel', back_populates='order_items')

class OrderDetailsModel(db.Model):
    __tablename__ = 'OrderDetails'

    OrderDetailID = db.Column(db.Integer, primary_key=True)
    CustomerID = db.Column(db.Integer, db.ForeignKey('Customers.CustomerID'))
    Total = db.Column(db.Float)
    CreatedAt = db.Column(db.DateTime)
    customer = db.relationship('CustomerModel', back_populates='order_details')
    order_items = db.relationship('OrderItemsModel', back_populates='order_detail')