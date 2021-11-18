import mysql.connector
from .config import server, user, password, db_name

def connect_db():
    conn = mysql.connector.connect(
        host=server,
        user=user,
        password=password,
        database=db_name
    )     
    return conn

#ďalšie funcie