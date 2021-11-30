import sqlalchemy as db
from .config import server, user, password, db_name

def connect_db():
    engine = db.create_engine(f'mysql+pymysql://{user}:{password}@{server}/{db_name}')
    return engine