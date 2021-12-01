import streamlit as st
from moduls.db import connect_db

def main():
    print('Apka beží')
    st.set_page_config(
        page_title="Krypto manager", 
        layout="wide", 
        page_icon="", 
        initial_sidebar_state="collapsed")
    conn = connect_db()
    mycursor = conn.cursor()
    
    st.title('Krypto evidencia')
    st.sidebar.subheader('hfkdshgf')
    col1,col2 = st.columns((3,1))
    col1.header('Hlavné okno')
    col1.subheader('nejaký text')
    col2.header("Nastavte parametre")

    sql_text= 'SELECT pohyby.kedy AS Dátum, pohyby.cena AS "Cena", pomocna.text AS "Smer",\
        pohyby.za_kolko AS "Za koľko", kryptomeny_1.nazov AS "Mena 1", kryptomeny_2.nazov AS "Mena 2", kryptomeny_1.skratka AS skratka1, kryptomeny_2.skratka AS skratka2\
        FROM pomocna, pohyby JOIN kryptomeny AS kryptomeny_1 ON kryptomeny_1.id = pohyby.mena1_id JOIN kryptomeny AS kryptomeny_2 ON kryptomeny_2.id = pohyby.mena2_id\
        WHERE pohyby.akcia_id = pomocna.id ORDER BY pohyby.akcia_id'

    #pohyby = []
    mycursor.execute(sql_text)
    myresult = mycursor.fetchall()
    #i = 0
    for x in myresult:
        print(x)
        
        col1.write(x)
        #pohyby.append(['datum']) = x[0] 
    #     i += 1
    # print(pohyby)


if __name__ == "__main__":
    main()

else:
    print('spustené ako modul')