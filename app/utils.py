import json
from app import db
from app.models import Offer, Order, User


def load_data(path):
    with open(path) as file:
        return json.load(file)


def load_offer(path):
    offers = load_data(path)

    for offer in offers:
        db.session.add(
            Offer(
                id=offer.get("id"),
                order_id=offer.get("order_id"),
                executor_id=offer.get("executor_id")
            )
        )

        db.session.commit()


def load_order(path):
    orders = load_data(path)

    for order in orders:
        db.session.add(Order(**order))

        db.session.commit()


def load_user(path):
    users = load_data(path)

    for user in users:
        db.session.add(
            User(
                **user
            )
        )

        db.session.commit()
