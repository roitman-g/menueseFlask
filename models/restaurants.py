import sys
sys.path.append('..')

from config import db, ma




ingredient_table = db.Table('ingredients',
                        db.Column('dish_id', db.Integer, db.ForeignKey('dish.id')),
                        db.Column('ingredient_id', db.Integer, db.ForeignKey('ingredient.id')))


class Ingredient(db.Model):
    __tablename__ = 'ingredient'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), primary_key=True)


class Dish(db.Model):
    __tablename__ = 'dish'
    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=True)
    ingredients = db.relationship('Ingredient', secondary=ingredient_table, backref='dishes')
    description = db.Column(db.Text())


class DishSchema(ma.Schema):
    class Meta:
        model = Dish


class Restaurant(db.Model):
    __tablename__ = 'restaurant'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(400))
    dishes = db.relationship('Dish', backref='restaurant')




class RestaurantSchema(ma.Schema):
    class Meta:
        model = Restaurant

        fields = ['id', 'name', 'description', 'dishes']


