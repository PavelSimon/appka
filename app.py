import streamlit as st
from moduls.functions import connect_db

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

    sql_text= 'SELECT pohyby.kedy as dátum, pohyby.mena1_id,pohyby.mena2_id,pohyby.za_kolko as "za koľko",pohyby.cena as "Jednotková cena",po.text as "Smer" FROM `pohyby`, `pomocna` po WHERE pohyby.akcia_id = po.id'

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