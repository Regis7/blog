# Modules
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
import streamlit.components.v1 as components
import pandas as pd
import numpy as np


# ----- PAGE CONFIGURATION ---
st.set_page_config(page_title="faduregis", page_icon=":tada:", layout = "wide")

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()  

# Function
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(df)

# --- COPY RIGHTS --

with st.container():
    left_column1, left_column2, right_column1, right_column2 = st.columns(4)
    with left_column1:
        st.write("---")
        st.write("@ Regis 2024")
    
    with left_column2:
        st.write("---")
        st.write("[LinkedIn >](https://www.linkedin.com/in/francoisregis/)")
        
    with right_column1:
        st.write("---")
        st.write("[Kaggle >](https://www.kaggle.com/faduregis)")
        
    with right_column2:
        st.write("---")
        st.write("[Github >](https://github.com/Regis7)")
      
