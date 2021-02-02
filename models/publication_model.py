from app import db

class Publication( db.Model ):
    id = db.Column( db.Integer, primary_key = True )
    title = db.Column( db.String( 50 ) )
    content = db.Column ( db.String( 255 ) )