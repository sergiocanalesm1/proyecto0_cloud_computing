from app import ma

class Event_Schema( ma.Schema ):
    class Meta:
        fields = ( "id", "name", "category", "place", "address", "start_date", "end_date", "is_virtual" )