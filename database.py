from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import os

from dotenv import load_dotenv
load_dotenv()

# I created the local database in the terminal with the following commands:
# $ psql
# $ CREATE DATABASE count_api;
# $ \q
URL_DATABASE = os.getenv('DATABASE_URL')

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
