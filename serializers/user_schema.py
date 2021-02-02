from app import ma

class User_Schema( ma.Schema ):
    class Meta:
        fields = ( "id", "username", "password" )