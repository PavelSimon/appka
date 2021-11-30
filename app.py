import streamlit as st
import sqlalchemy as db
from sqlalchemy.orm import aliased
import pandas as pd
from moduls.orm import conn, pohyby, users, kryptomeny, burzy, pomocna

def main():
    print('Apka beží')
    st.set_page_config(
        page_title="Krypto manager", 
        layout="wide", 
        page_icon="", 
        initial_sidebar_state="collapsed")

    st.title('Krypto evidencia')
    st.sidebar.subheader('hfkdshgf')
    col1,col2 = st.columns((3,1))
    col1.header('Hlavné okno')
    col1.subheader('nejaký text')
    col2.header("Nastavte parametre")

    mena1 = aliased(kryptomeny)
    mena2 = aliased(kryptomeny)

    query = db.select(
        [pohyby.c.cena.label('Cena'),
        pomocna.c.text.label('Smer'),
        pohyby.c.za_kolko.label('Za koľko'), 
        mena1.c.nazov.label('Mena 1'),
        mena2.c.nazov.label('Mena 2'),
        mena1.c.skratka,
        mena2.c.skratka
        ]
        ).where(
            pohyby.c.akcia_id==pomocna.c.id
        ).join(
            mena1, mena1.c.id == pohyby.c.mena1_id
        ).join(
            mena2, mena2.c.id == pohyby.c.mena2_id
        ).order_by(
            pohyby.c.akcia_id
        )

    print(f'qeury:{query}')
    ResultSet = conn.execute(query).fetchall()
    df = pd.DataFrame(ResultSet)
    df.columns = ResultSet[0].keys()
    df['Menový pár']=df['skratka']+'/'+df['skratka_1']
    
    col1.table(df)

if __name__ == "__main__":
    main()

else:
    print('spustené ako modul')