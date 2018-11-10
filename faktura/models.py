from datetime import datetime
from faktura import db


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"Customer('{self.first_name}', '{self.last_name}', '{self.email}')"


class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    inStock = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Customer('{self.id}', '{self.name}', '{self.inStock}')"


class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customerId = db.Column(db.Integer, ForeignKey("Customer.id"))
    email = db.Column(db.String(20), unique=True, nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"Customer('{self.first_name}', '{self.last_name}', '{self.email}')"


class Settings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    companyName = db.Column(db.String(30), nullable=False)
    companyAddress = db.Column(db.String(20), nullable=False)
    companyEmail = db.Column(db.String(20), unique=True, nullable=False)
    companyPhone = db.Column(db.Integer, nullable=False)
    companyMobile = db.Column(db.Integer, nullable=False)
    companyZip = db.Column(db.Integer, nullable=False)
    companyCity = db.Column(db.String(20), unique=True, nullable=False)
    companyNumber = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"Customer('{self.first_name}', '{self.last_name}', '{self.email}')"
