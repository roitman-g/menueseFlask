from flask_restful import Resource, fields, reqparse
import sys
sys.path.append('..')




from flask import jsonify, request



from models.restaurants import Restaurant

from models.restaurants import RestaurantSchema

from config import db


restaurant_args_parser = reqparse.RequestParser()
restaurant_args_parser.add_argument('name')
restaurant_args_parser.add_argument('description')

class RestaurantList(Resource):
    def get(self):
        print('I  getting all the restaurants')
        all_restaurants = Restaurant.query.all()
        # all_restaurants = db.session.query(Restaurant).all()
        print(all_restaurants)
        restaurants_schema = RestaurantSchema(many=True)

        result = restaurants_schema.dumps(all_restaurants)

        return jsonify(result.data)

    def post(self):
        print('Posting the restaurant')
        args = restaurant_args_parser.parse_args()
        name = args['name']
        description = args['description']
        print('This is the name of the restaurant {} and this is the description {}'.format(name, description))

        print('Going further')

        new_restaurant = Restaurant()
        new_restaurant.name = name
        new_restaurant.description = description

        print('The model was created. Name: {}, Description: {}'.format(name, description))

        db.session.add(new_restaurant)
        db.session.commit()

        return "Restaurant is successfully added"


class Restaurants(Resource):
    def get(self, id):
        rest_schema = RestaurantSchema()
        restaurant = Restaurant.query.filter_by(id='id')

        return rest_schema.jsonify(restaurant)

    def delete(self, id):
        restaurant = Restaurant.query.filter_by(id='id')

        db.session.delete(restaurant)

        return "Restaurant deleted"

    def put(self, id):

        changings = request.args

        restaurant = Restaurant.query.filter_by(id='id')

        for key, value in changings.items():
            setattr(restaurant, key, value)

        return "Success"




