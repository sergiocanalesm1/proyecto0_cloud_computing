from flask_restful import Resource, request

from models.publication_model import Publication
from serializers.publication_schema import Publication_Schema
from app import db

class PublicationAPI:
    def __init__( self ):
        self.posts_schema = Publication_Schema( many = True )
        self.post_schema = Publication_Schema()

class MultiplePublicationResource( PublicationAPI, Resource ):
    def __init__( self ):
        super().__init__()

    def get( self ):
        publications = Publication.query.all()
        return self.posts_schema.dump( publications )

    def post( self ):
        new_publication = Publication(
            title = request.json[ "title" ],
            content = request.json[ "content" ]
        )
        db.session.add( new_publication )
        db.session.commit()
        return self.post_schema.dump( new_publication )

class SinglePublicationResource( PublicationAPI, Resource ):
    def __init__( self ):
        super().__init__()

    def get( self, id ):
        publication = Publication.query.get_or_404( id )
        return self.post_schema.dump( publication )

    def put( self, id ):
        publication = Publication.query.get_or_404( id )
        if "title" in request.json:
            publication.title = request.json[ "title" ]
        if "content" in request.json:
            publication.content = request.json[ "content" ]
        db.session.commit()
        return self.post_schema.dump( publication )

    def delete( self, id ):
        publication = Publication.query.get_or_404( id )
        db.session.delete( publication )
        db.session.commit()
        return "", 204
