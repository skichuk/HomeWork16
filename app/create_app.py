from flask import Flask

from app import db
from app.utils import load_offer, load_user, load_order

app = Flask(__name__)


def create_app():
    app.config['SQLAlCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
    app.config['RESTX_JSON'] = {'ensure_ascii': False, 'indent': 4}

    with app.app_context():
        db.init_app(app)
        db.drop_all()
        db.create_all()

        offer = load_offer('/home/syrbor/PycharmProjects/HomeWork16/data/offers.json')
        user = load_user('/home/syrbor/PycharmProjects/HomeWork16/data/user.json')
        order = load_order('/home/syrbor/PycharmProjects/HomeWork16/data/orders.json')
    return app


app = create_app()

