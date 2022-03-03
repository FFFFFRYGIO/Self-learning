from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database
from local_settings import postgresql as settings

import logging

log = logging.getLogger(__name__)

def get_database():
    #connect to db
    try:
        engine = get_engine_from_settings()
        log.info("Connected to db")
    except IOError:
        log.exception("Failed connection")
        return None, 'fail'
    
    return engine

def get_engine_from_settings():
    #set db connection based on "local_settings.py"
    keys = ['pguser','pgpasswd','pghost','pgport','pgdb']
    if not all(key in keys for key in settings.keys()):
        raise Exception('Bad config file')
    return get_engine(
        settings['pguser'],
        settings['pgpasswd'],
        settings['pghost'],
        settings['pgport'],
        settings['pgdb'],
        )

def get_engine(user, passwd, host, port, db):
    #get sqlalchemy engine
    url = f"postgresql://{user}:{passwd}@{host}:{port}/{db}"
    if not database_exists(url):
        create_database(url)
    engine = create_engine(url, pool_size=50, echo=False)
    return engine

def get_session():
    #creates user session
    engine = get_engine_from_settings()
    session = sessionmaker(bind=engine)()
    return session

db = get_database()
session = get_session()
Base = declarative_base()