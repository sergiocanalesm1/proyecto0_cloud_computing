from flask_restful import Resource, request
#from flask_jwt_extended import create_access_token

from app import db
from serializers.user_schema import User_Schema
from models.user_model import User


class RegistryAPI(Resource):
    def __init__( self ):
        self.post_schema = User_Schema()

    def post( self ):
        if self._getUsername( request.json[ "username" ] ) is not None:
            return { "message" : "Please register with a non existing username" }, 400
        new_user = User(
            username = request.json[ "username" ],
            password = request.json[ "password" ]
        )
        #token = create_access_token( identity = request.json[ "username" ] )
        db.session.add( new_user )
        db.session.commit()
        return self.post_schema.dump( new_user )

    def get( self ):
        user = self._getUser( request.json[ "username" ], request.json[ "password" ] )
        if user is None:
            return { "message" : "No user found with those credentials" }, 400
        return self.post_schema.dump( user )
    def _getUsername( self, username ):
        for row in User.query.all():
            if row.username == username:
                return row


class LoginAPI( Resource ):
    def __init__( self ):
        self.post_schema = User_Schema()

    def post( self ):
        user = self._getUser( request.json[ "username" ], request.json[ "password" ] )
        if user is None:
            return { "message" : "No user found with those credentials" }, 400
        return self.post_schema.dump( user )

    def _getUser( self, username, password ):
        for row in User.query.all():
            if row.username == username and row.password == password:
                return row