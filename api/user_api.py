from flask_restful import Resource, request
#from flask_jwt_extended import create_access_token

from app import db
from serializers.user_schema import User_Schema
from models.user_model import User


class UserAPI( Resource ):
    def __init__( self ):
        self.post_schema = User_Schema()

    def post( self ):
        if self.getUsername( request ) is not None:
            return { "message" : "Please register with a non existing user" }, 400
        new_user = User(
            username = request.json[ "username" ],
            password = request.json[ "password" ]
        )
        #token = create_access_token( identity = request.json[ "username" ] )
        db.session.add( new_user )
        db.session.commit()
        return self.post_schema.dump( new_user )

    def get( self ):
        user = self.getUser( request )
        if user is None:
            return { "message" : "No user found with those credentials" }, 400
        return self.post_schema.dump( user )

    def getUser( self, request ):
        for row in User.query.all():
            if row.username == request.json[ "username" ] and row.password == request.json[ "password" ]:
                return row
    def getUsername( self, request ):
        for row in User.query.all():
            if row.username == request.json[ "username" ]:
                return row