import sqlalchemy as db
from sqlalchemy.orm import aliased
import pandas as pd
from .orm import conn, pohyby, users, kryptomeny, burzy, pomocna

def data():
    mena1 = aliased(kryptomeny)
    mena2 = aliased(kryptomeny)

    query = db.select(
        [pohyby.c.cena.label('Cena'),
        pomocna.c.text.label('Smer'),
        pohyby.c.za_kolko.label('Za koľko'), 
        mena1.c.nazov.label('Mena 1'),
        mena2.c.nazov.label('Mena 2'),
        mena1.c.skratka.label('skratka1'),
        mena2.c.skratka.label('skratka2')
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

    # print(f'qeury:{query}')
    ResultSet = conn.execute(query).fetchall()
    df = pd.DataFrame(ResultSet)
    df.columns = ResultSet[0].keys()
    df['Menový pár']=df['skratka1']+'/'+df['skratka2']
    
    return df