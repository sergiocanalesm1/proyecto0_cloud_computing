from flask import Flask
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager


app = Flask( __name__ )

cors = CORS( app )
jwt = JWTManager( app )
db = SQLAlchemy( app )
ma = Marshmallow( app )

app.config['JWT_SECRET_KEY'] = 'super-secret'
app.config['CORS_HEADERS'] = 'Content-Type'
#app.config[ 'JWT_ROUTER_API_NAME' ] = "/api/v1"
app.config[ 'SQLALCHEMY_DATABASE_URI' ] = 'sqlite:///test.db'




