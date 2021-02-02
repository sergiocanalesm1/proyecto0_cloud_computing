from sqlalchemy.orm import relationship

from app import db


class User( db.Model ):
    __tablename__ = "user"
    id = db.Column( db.Integer, primary_key = True )
    username = db.Column( db.String( 20 ) )
    password = db.Column( db.String( 20 ) )
    events = relationship( "Event", cascade = "all, delete" )