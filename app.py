from config import api,app, db

from routes.restaurants import Restaurants, RestaurantList

def add_restaurant_api():
     api.add_resource(RestaurantList, '/restaurants/')
     api.add_resource(Restaurants, '/restaurants/<id>')


if __name__ == '__main__':
    add_restaurant_api()
    db.create_all()
    print('Created a database...')
    app.run(debug=True)


