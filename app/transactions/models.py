import datetime
from sqlalchemy.orm import relationship
from app import db


class Transactions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    transaction_type_id = db.Column(db.Integer, db.ForeignKey('transaction_types.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=True)
    amount = db.Column(db.Numeric, nullable=False)
    date = db.Column(db.Date, nullable=False)

    transaction_type = relationship('TransactionTypes', backref='transaction_types')
    category = relationship('Categories', backref='categories')

    def __init__(self, transaction_type, name, amount, date, category=None):
        self.transaction_type = transaction_type
        self.name = name
        if category is not None:
            self.category = category
        self.amount = amount
        self.date = self.str_to_datetime(date)

    @staticmethod
    def str_to_datetime(date: str) -> datetime.date:
        return datetime.datetime.strptime(date, "%m/%d/%Y").date()

    def set_date(self, date: str):
        self.date = self.str_to_datetime(date)

    def get_date(self) -> str:
        return self.date.strftime("%m/%d/%Y")

    def to_json(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'transaction_type': self.transaction_type.id,
            'category': self.category.id,
            'amount': self.amount,
            'date': self.get_date(),
        }


class TransactionTypes(db.Model):
    __tablename__ = 'transaction_types'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __init__(self, name):
        self.name = name
