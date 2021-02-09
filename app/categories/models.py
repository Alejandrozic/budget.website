from app import db


class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __init__(self, name):
        self.name = name

    def to_json(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
        }
