from homerwor_programing_innodom.innodom_SQLAlchemy.db_connect import DBConnector
from homerwor_programing_innodom.innodom_SQLAlchemy.db_engine import db_url
from homerwor_programing_innodom.innodom_SQLAlchemy.models import User, Balance

front_user_data = [
    {
    "id": 1,
    "name": "Peter",
    "surname": "Smith",
    "age": 34,
    "email": "petersmith@gmail.com"
},
{
    "id": 2,
    "name": "John",
    "surname": "Doe",
    "age": 25,
    "email": "johndoe@example.com"
},
{
    "id": 3,
    "name": "Mary",
    "surname": "Johnson",
    "age": 42,
    "email": "maryjohnson@yahoo.com"
},
{
    "id": 4,
    "name": "Susan",
    "surname": "Williams",
    "age": 30,
    "email": "susanwilliams@hotmail.com"
},
{
    "id": 5,
    "name": "David",
    "surname": "Brown",
    "age": 28,
    "email": "davidbrown@outlook.com"
},
{
    "id": 6,
    "name": "Elizabeth",
    "surname": "Green",
    "age": 36,
    "email": "elizabethgreen@gmail.com"
}]

front_balance_from_date = [
{
    "id": 1,
    "user_balance": 1000.00,
    "user_id": 1,
    "create_at": "2023-08-01"
},
{
    "id": 2,
    "user_id": 2,
    "user_balance": 1000.00,
    "create_at": "2023-08-01"
},
{
    "id": 3,
    "user_id": 2,
    "user_balance": 1100.00,
    "create_at": "2023-08-02"
},
{
    "id": 4,
    "user_id": 2,
    "user_balance": 1200.00,
    "create_at": "2023-08-03"
},
{
    "id": 5,
    "user_id": 3,
    "user_balance": 500.00,
    "create_at": "2023-09-01"
},
{
    "id": 6,
    "user_id": 3,
    "user_balance": 600.00,
    "create_at": "2023-09-02"
}]


#
def create_new_user(manager, form_data):
    try:
        user = User(**form_data)
        manager.add(user)
        manager.commit()
    except Exception as e:
        print(e)
        manager.rollback()


def write_user_balance(manager, form_data):
    try:
        balance = Balance(**form_data)
        manager.add(balance)
        manager.commit()
    except Exception as e:
        print(e)
        manager.rollback()


with DBConnector(db_url=db_url) as session:
    create_new_user(manager=session, form_data=front_user_data)
    write_user_balance(manager=session, form_data=front_balance_from_date)
