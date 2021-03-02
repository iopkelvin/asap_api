import os

from flask import Flask
from flask_restful import Api
# from flask_jwt import JWT  # Security
# from security import authenticate, identity  # Modules for JWT
from resources.member import MemberId, MemberList
from resources.validate import Validate

from flask_caching import Cache
config = {"CACHE_TYPE": "simple",
          "CACHE_DEFAULT_TIMEOUT": 30
          }
app = Flask(__name__)

app.config['DEBUG'] = True  # debug for error messages (html page)

# SQLAlchemy will use the database created at root or sqlite
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
# Turns off Flask SQL Alchemy modification tracker, not the library's
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Allows flask extensions to raise their own exceptions/errors
app.config['PROPAGATE_EXCEPTIONS'] = True

# Added 30 seconds caching
app.config.from_mapping(config)
app.cache = Cache(app)

app.secret_key = 'kelvin'
api = Api(app)

# jwt = JWT(app, authenticate, identity)  # auth

api.add_resource(MemberId, '/<int:member_id>')  # http://127.0.0.1:5000/..
api.add_resource(Validate, '/validate')
api.add_resource(MemberList, '/members')

if __name__ == '__main__':
    # If app.py is run, then the following will be run.
    from db import db
    db.init_app(app)

    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()

    app.run(port=5000)