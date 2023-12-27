from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    TIMESTAMP,
    Boolean,
    ForeignKey,
    func
)
from sqlalchemy.orm import (
    relationship,
    declarative_base
)
from sqlalchemy import text
from homerwor_programing_innodom.innodom_SQLAlchemy.db_connect import DBConnector
import os
import environ
from urllib.parse import quote

BASE_DIR = '/home/diana/Desktop/Python/тренировка/homerwor_programing_innodom/innodom_SQLAlchemy'
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.evn'))
db_url = f"postgresql://{env('DB_USER_POS')}:{quote(env('DB_PASSWORD_POS'))}@{env('DB_HOST_POS')}:{env('DB_PORT_POS')}/{env('DB_NAME_POS')}"

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False)
    surname = Column(String(30))
    age = Column(Float)
    email = Column(String(100), unique=True, nullable=False)
    create_at = Column(TIMESTAMP, server_default=func.current_timestamp())
    updated_at = Column(TIMESTAMP)
    delete = Column(Boolean, server_default='False')


class Balance(Base):
    __tablename__ = 'balance'

    id = Column(Integer, primary_key=True)
    user_balance = Column(Float, server_default=text("CAST(0 AS FLOAT)"))
    user_id = Column(Integer, ForeignKey('user.id'))
    create_at = Column(TIMESTAMP, server_default=func.current_timestamp())
    updated_at = Column(TIMESTAMP)
    delete = Column(Boolean, server_default='False')


if __name__ == "__main__":
    db_connector = DBConnector(db_url=db_url)
    db_connector.create_tables(Base)
