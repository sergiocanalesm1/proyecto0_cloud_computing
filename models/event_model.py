from app import db


def is_category( category ):
    return category in [ "CONFERENCIA", "SEMINARIO", "CONGRESO", "CURSO" ]


class Event( db.Model ):
    __tablename__ = "event"
    id = db.Column( db.Integer, primary_key = True )
    name = db.Column( db.String( 50 ) )
    category = db.Column( db.String( 30 ) )
    place = db.Column( db.String( 50 ) )
    address = db.Column( db.String( 30 ) )
    start_date = db.Column( db.DateTime )
    end_date = db.Column( db.DateTime )
    is_virtual = db.Column( db.Boolean )
    user_id = db.Column( db.Integer, db.ForeignKey( "user.id" ) )

