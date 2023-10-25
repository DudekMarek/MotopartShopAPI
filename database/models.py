from api.main import db

class Customer(db.Model):
    __tablename__ = 'Customers'

    CustomerID = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(50), index=True)
    LastName = db.Column(db.String(50))
    Email = db.Column(db.String(100))
    Phone = db.Column(db.String(20))
    Address = db.Column(db.String(255))
    order_details = db.relationship('OrderDetails', back_populates='customer')

class Product(db.Model):
    __tablename__ = 'Products'

    ProductID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100))
    Description = db.Column(db.Text)
    Price = db.Column(db.Float)
    QuantityInStock = db.Column(db.Integer)
    order_items = db.relationship('OrderItems', back_populates='product')

class OrderItems(db.Model):
    __tablename__ = 'OrderItems'

    OrderItemID = db.Column(db.Integer, primary_key=True)
    ProductID = db.Column(db.Integer, db.ForeignKey('Products.ProductID'))
    Quantity = db.Column(db.Integer)
    OrderDetailID = db.Column(db.Integer, db.ForeignKey('OrderDetails.OrderDetailID'))
    product = db.relationship('Product', back_populates='order_items')
    order_detail = db.relationship('OrderDetails', back_populates='order_items')

class OrderDetails(db.Model):
    __tablename__ = 'OrderDetails'

    OrderDetailID = db.Column(db.Integer, primary_key=True)
    CustomerID = db.Column(db.Integer, db.ForeignKey('Customers.CustomerID'))
    Total = db.Column(db.Float)
    CreatedAt = db.Column(db.DateTime)
    customer = db.relationship('Customer', back_populates='order_details')
    order_items = db.relationship('OrderItems', back_populates='order_detail')