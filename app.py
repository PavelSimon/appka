import streamlit as st
from moduls.functions import connect_db

def main():
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

    mycursor.execute("SELECT * FROM users")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
        col1.write(x)

if __name__ == "__main__":
    main()

else:
    print('spustené ako modul')