import streamlit as st
from moduls.config import server, user, password, db_name

print(server)

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