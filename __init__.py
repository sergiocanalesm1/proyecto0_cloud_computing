from api.base_api import BaseAPI
from app import app


if __name__ == '__main__':
    """
    db.drop_all()
    db.create_all()
    """
    api = BaseAPI()
    app.run()