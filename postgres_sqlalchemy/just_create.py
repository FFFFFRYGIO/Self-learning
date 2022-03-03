from local_settings import admin_login_data as settings
from sqlalchemy_utils import database_exists, create_database

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
    url = f"postgresql://{user}:{passwd}@{host}:{port}/{db}"
    if not database_exists(url):
        create_database(url)

get_engine_from_settings()