import os
from urllib.parse import quote
import environ
from sqlalchemy.exc import DisconnectionError
from homerwor_programing_innodom.innodom_SQLAlchemy.db_connect import DBConnector
from homerwor_programing_innodom.innodom_SQLAlchemy.models import User, Balance

BASE_DIR = '/home/diana/Desktop/Python/тренировка/homerwor_programing_innodom/innodom_SQLAlchemy'
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.evn'))
db_url = f"postgresql://{env('DB_USER_POS')}:{quote(env('DB_PASSWORD_POS'))}@{env('DB_HOST_POS')}:{env('DB_PORT_POS')}/{env('DB_NAME_POS')}"

front_user_data = {
    "id": 1,
    "name": "Peter",
    "surname": "Smith",
    "age": 34,
    "email": "petersmith@gmail.com"
}

front_balance_from_date = {"id": 1, "user_balance": "df", "user_id": 1}


#
def create_new_user(manager, form_data):
    try:
    user = User(**form_data)

    manager.add(user)
    raise DisconnectionError("Something went wrong")

    manager.commit()


def write_user_balance(manager, form_data):
    balance = Balance(**form_data)

    manager.add(balance)

    manager.commit()


with DBConnector(db_url=db_url) as session:
    try:
        create_new_user(manager=session, form_data=front_user_data)
        write_user_balance(manager=session, form_data=front_balance_from_date)
    except DisconnectionError as e:
        print(e)
        session.rollback()
    except Exception as e:
        print(e)
