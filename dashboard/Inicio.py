"""
Esta corresponde a la pagina de inicio
"""

import streamlit as st

from PIL import Image

# Se configura la cabecera del 
st.set_page_config(
    page_title="Demo Sacyr",
    page_icon="🛣️",
    layout = "wide"
)
logo_alaya = Image.open("../images/LogoAlaya.png")
st.image(logo_alaya,width =300)



st.write("# Bienvenido al demo Sacyr")

st.sidebar.success("Seleccióne una Funcionalidad.")