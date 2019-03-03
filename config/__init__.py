from flask import Flask
from flask_restful import Api
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sys
sys.path.append('..')



app = Flask(__name__)
USERNAME = 'root'
PASSWORD = 'NanoNano2580'
NAME = 'Menuese'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@localhost/{}'.format(USERNAME, PASSWORD, NAME)

db = SQLAlchemy(app)
api = Api(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)

app.config['SECRET_KEY'] = 'the quick brown fox jumps over the laziest dog in the world'

app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True