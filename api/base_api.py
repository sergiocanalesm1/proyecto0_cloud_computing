from flask_restful import Api

import api.publications_api as publication_api
from app import app


class BaseAPI():
    def __init__( self ):
        api = Api( app )
        api.add_resource( publication_api.MultiplePublicationResource, '/publications' )
        api.add_resource( publication_api.SinglePublicationResource, '/publications/<int:id>' )