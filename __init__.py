from api.base_api import BaseAPI
from app import app


if __name__ == '__main__':
    api = BaseAPI()
    app.run( debug = True )