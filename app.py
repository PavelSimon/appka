import streamlit as st
import sqlalchemy as db
import pandas as pd
from moduls.orm import connect_db
from moduls.config import server, user, password, db_name

def main():
    print('Apka beží')
    st.set_page_config(
        page_title="Krypto manager", 
        layout="wide", 
        page_icon="", 
        initial_sidebar_state="collapsed")


    engine = db.create_engine(f'mysql+pymysql://{user}:{password}@{server}/{db_name}')
    connection = engine.connect()
    # print(f'engine:{engine}, connection: {connection}')
    metadata = db.MetaData()
    users = db.Table('users',metadata,autoload=True, autoload_with=engine)
    pomocna = db.Table('pomocna',metadata,autoload=True, autoload_with=engine) 
    kryptomeny = db.Table('kryptomeny',metadata,autoload=True, autoload_with=engine) 
    burzy = db.Table('burzy',metadata,autoload=True, autoload_with=engine) 
    pohyby = db.Table('pohyby',metadata,autoload=True, autoload_with=engine) 


    st.title('Krypto evidencia')
    st.sidebar.subheader('hfkdshgf')
    col1,col2 = st.columns((3,1))
    col1.header('Hlavné okno')
    col1.subheader('nejaký text')
    col2.header("Nastavte parametre")

    query = db.select(
        [pohyby.c.cena,
        pomocna.c.text,
        pohyby.c.za_kolko, 
        pohyby.c.mena1_id, 
        kryptomeny.c.nazov,
        pohyby.c.mena2_id
        ]
        ).where(
            pohyby.c.akcia_id==pomocna.c.id, 
            pohyby.c.mena1_id == kryptomeny.c.id
        ).order_by(
            pohyby.c.akcia_id
        )

    print(f'qeury:{query}')

    ResultSet = connection.execute(query).fetchall()
    # df = pd.DataFrame(ResultSet)
    # df.columns = ResultSet[0].keys()
    # df.head()
    print(f'SQL výsledok:{ResultSet}')
    
    #i = 0
    for x in ResultSet:
        print(x)
        
        col1.write(x)
    #    #pohyby.append(['datum']) = x[0] 
    # #     i += 1
    # # print(pohyby)


if __name__ == "__main__":
    main()

else:
    print('spustené ako modul')