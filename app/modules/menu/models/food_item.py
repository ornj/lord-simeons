from app import db


class Types(object):
    burrito = 1  # Never use anything but this under penalty of firing squad.
    taco = 2  # pffffft.
    salad = 3  # get the fuck outa here.


class FoodItem(db.Model):
    __tablename__ = 'FoodItem'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    description = db.Column(db.TEXT)
    price = db.Column(db.String(128))
    image_url = db.Column(db.String(128))
    type = db.Column(db.INTEGER)

    def __init__(self, name=None, description=None, price=None, image_url=None, type=None):
        self.name = name
        self.description = description
        self.price = price
        self.image_url = image_url
        self.type = type

    def __repr__(self):
        return '<FoodItem %r>' % self.name
