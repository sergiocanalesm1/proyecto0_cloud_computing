from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager


app = Flask( __name__ )

app.config['JWT_SECRET_KEY'] = 'super-secret'
app.config[ 'WHITE_LIST_ROUTES' ] = [
    ( "PUT", "/auth/user/<int:user_id>" ),
    ( "GET", "/auth/user" ),
    ( "POST", "/auth/user" )
]
#app.config[ 'JWT_ROUTER_API_NAME' ] = "/api/v1"
app.config[ 'SQLALCHEMY_DATABASE_URI' ] = 'sqlite:///test.db'

jwt = JWTManager( app )
db = SQLAlchemy( app )
ma = Marshmallow( app )




