import datetime

from flask_restful import Resource, request

from app import db
from serializers.event_schema import Event_Schema
from models.event_model import Event


class SingleEventAPI( Resource ):
    """
    listar en descendente con start date
    get single ----------- id
    post
    put
    delete
    """
    def  __init__( self ):
        self.post_schema = Event_Schema()

    def get( self, id ):
        event = Event.query.get_or_404( id )
        return self.post_schema.dump( event )



    def put( self, id ):
        event = Event.query.get_or_404( id )
        if "id" in request.json:
            event.id = request.json[ "id" ]
        if "name" in request.json:
            event.name = request.json[ "name" ]
        if "category" in request.json:
            event.category = request.json[ "category" ]
        if "place" in request.json:
            event.place = request.json[ "place" ]
        if "address" in request.json:
            event.address = request.json[ "address" ]
        if "start_date" in request.json:
            event.start_date = datetime.datetime.strptime( request.json[ "start_date" ], '%Y-%m-%d %H:%M:%S.%f' ),
        if "end_date" in request.json:
            event.end_date = datetime.datetime.strptime( request.json[ "end_date" ], '%Y-%m-%d %H:%M:%S.%f' ),
        if "is_virtual" in request.json:
            event.is_virtual = request.json[ "is_virtual" ]
        if "user_id" in request.json:
            event.user_id = request.json[ "user_id" ]
        db.session.commit()
        return self.post_schema.dump( event )

    def delete( self, id ):
        event = Event.query.get_or_404( id )
        db.session.delete( event )
        db.session.commit()
        return { "message" : "successfully deleted"}, 204

class MultipleEventAPI( Resource ):
    def __init__( self ):
        self.post_schema = Event_Schema()
        self.posts_schema = Event_Schema( many = True )

    def post( self ):
        new_event = Event(
            id = request.json[ "id" ],
            name = request.json[ "name" ],
            category = request.json[ "category" ],
            place = request.json[ "place" ],
            address = request.json[ "address" ],
            start_date = datetime.datetime.strptime( request.json[ "start_date" ], '%Y-%m-%d %H:%M:%S.%f' ),
            end_date = datetime.datetime.strptime( request.json[ "end_date" ], '%Y-%m-%d %H:%M:%S.%f' ),
            is_virtual = request.json[ "is_virtual" ],
            user_id = request.json[ "user_id" ]
        )
        db.session.add( new_event )
        db.session.commit()
        return self.post_schema.dump( new_event )

    def get( self ):
        events = list( Event.query.all() )
        events.sort( key = lambda event: event.start_date, reverse = True )
        return self.posts_schema.dump( events )