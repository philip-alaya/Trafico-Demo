import streamlit as st
import numpy as np
import time
from pickle import load
import os
import pandas as pd
from PIL import Image
import pickle

st.set_page_config(
    page_title="Exploración Data",
    page_icon="🛣️",
    layout = "wide"
)

# col_logo1, col_titulo, col_logo2 = st.columns([2, 6, 2])

logo_alaya = Image.open("../images/LogoAlaya.png")
st.image(logo_alaya,width =300)