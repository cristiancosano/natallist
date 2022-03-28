from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from app.config.environment import initialize_environment
import os


def register_database():
    initialize_environment()
    username = os.getenv('DB_USERNAME')
    password = os.getenv('DB_PASSWORD')
    server = os.getenv('DB_HOST')
    db_name = os.getenv('DB_DATABASE')
    port = os.getenv('DB_PORT')

    created_engine = create_engine(f'mysql+pymysql://{username}:{password}@{server}:{port}/{db_name}')

    local_session = sessionmaker(autocommit=False, autoflush=False, bind=created_engine)
    db_session = scoped_session(local_session)
    base = declarative_base()
    base.query = db_session.query_property()
    return base, local_session, created_engine


Base, LocalSession, engine = register_database()
