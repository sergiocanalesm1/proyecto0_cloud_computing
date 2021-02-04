from flask_restful import Api

import api.user_api as user_api
import api.event_api as event_api
from app import app


class BaseAPI():
    def __init__( self ):
        api = Api( app )
        api.add_resource(user_api.RegistryAPI, '/auth')
        api.add_resource(user_api.LoginAPI, '/user')
        api.add_resource(event_api.EventAPI, '/events')
        api.add_resource( event_api.SingleEventAPI, '/event/<int:id>' )
        api.add_resource(event_api.UserEventAPI, '/user_events/<int:id>')

        #api.add_resource( publication_api.MultiplePublicationResource, '/publications' )
        #api.add_resource( publication_api.SinglePublicationResource, '/publications/<int:id>' )