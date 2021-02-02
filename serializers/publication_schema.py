from app import ma

class Publication_Schema( ma.Schema ):
    class Meta:
        fields = ( "id", "title", "content" )