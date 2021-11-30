import sqlalchemy as db
from .config import server, user, password, db_name

engine = db.create_engine(f'mysql+pymysql://{user}:{password}@{server}/{db_name}')
conn = engine.connect()

metadata = db.MetaData()
users = db.Table('users',metadata,autoload=True, autoload_with=conn)
pomocna = db.Table('pomocna',metadata,autoload=True, autoload_with=conn) 
kryptomeny = db.Table('kryptomeny',metadata,autoload=True, autoload_with=conn) 
burzy = db.Table('burzy',metadata,autoload=True, autoload_with=conn) 
pohyby = db.Table('pohyby',metadata,autoload=True, autoload_with=conn) 