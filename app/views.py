import json
from flask import request, Flask
from app.models import User
from flask_sqlalchemy import SQLAlchemy

from app.utils import load_offer, load_user, load_order

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app. config['RESTX_JSON'] = {'ensure_ascii': False, 'indent': 4}
db = SQLAlchemy(app)

offer_data = load_offer('/home/syrbor/PycharmProjects/HomeWork16/data/offers.json')
user_data = load_user('/home/syrbor/PycharmProjects/HomeWork16/data/user.json')
order_data = load_order('/home/syrbor/PycharmProjects/HomeWork16/data/orders.json')

@app.route('/users', methods=['GET', 'POST'])
def get_users():
    if request.method == 'GET':
        result = []
        for user in db.session.query(User).all():
            result.append(user.return_data())
        return app.request_class(json.dumps(result), mimetype="application/json", status=200)

    if request.method == 'POST':
        data = request.json
        db.session.add(User(**data))
        return app.request_class(json.dumps("OK"), mimetype="application/json", status=200)


if __name__ == '__main__':
    app.run("localhost", port=8080)
