from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.orm import declarative_base
from os import environ
from dotenv import load_dotenv

load_dotenv()

db_user = environ.get('CALC_DB_USER')
db_passwd = environ.get('CALC_DB_PASSWORD')
db_host = environ.get('CALC_DB_HOST')
db_port = environ.get('CALC_DB_PORT')
db_name = environ.get('CALC_DB_NAME')

DATABASE_URL = f"postgresql://{db_user}:{db_passwd}@{db_host}:{db_port}/{db_name}"

engine = create_engine(DATABASE_URL)

Base = declarative_base()


class Coefficient(Base):
    __tablename__ = "coefficients"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    value = Column(Float)
