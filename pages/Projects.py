import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
import streamlit.components.v1 as components

# ----- PAGE CONFIGURATION ---
st.set_page_config(page_title="faduregis", page_icon=":tada:", layout = "wide")

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()  

# ---- HEADER SECTION ----
with st.container():
    st.title("Currently busy with below projects")
    st.write(""" 
As someone involved in technology, I endeavor to oversee as many tech projects as I can to continuously navigate the landscape of opportunities.""")

# --- LOAD ASSETS ---

img_contact_form = Image.open("images/FaduTech_Logo.png")
img_process_view = Image.open("images/process view.png")

   
# ---- PROJECT ---

with st.container():
    st.write("---")
    st.header("My projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        # insert image
        st.image(img_contact_form)
        st.write("##")
        st.write("##")
        #st.image(img_process_view)

    with text_column:
        st.write("Tech service provider")
        st.write(
             """
            - FADU Tech is an emerging mobile and web application development, data and web hosting company in Rwanda. It has a vision of becoming one of the leading mobile and web application development companies in Africa. We make sure that we have the latest trends and technologies at hand. FADU Tech has well experienced employees in the tech filed.
            """
        )
        st.write("[Read more >](https://fadu.co.rw/)")
        st.write("##")
    
    with text_column:
        st.write("Hosting service provider")
        st.write(
             """
            - FADU Tech is an emerging mobile and web application development, data and web hosting company in Rwanda. It has a vision of becoming one of the leading mobile and web application development companies in Africa. We make sure that we have the latest trends and technologies at hand. FADU Tech has well experienced employees in the tech filed.
            """
        )
        st.write("[Read more >](https://faduhost.com/)")
        st.write("##")

        st.write("Blogging")
        st.write(
            """
            - After ten years in the tech industry, working in Africa and Europe for research institutions,
            companies, and organizations, I thought about how I could contribute to the wider community to
            leverage tech use in our daily activities. Techadvisors was created to help reach a wide audience and
            share our experiences. After a while of posting tech tips on the web, many tech practitioners joined.

            - A group of committed tech lovers contribute to the posts we publish on this platform.
            """
        )
        st.write("[Read more >](https://techadvisors.nl/)")
        
# --- COPY RIGHTS --

with st.container():
    left_column1, left_column2, right_column1, right_column2 = st.columns(4)
    with left_column1:
        st.write("---")
        st.write("@ Regis 2024")
    
    with left_column2:
        st.write("---")
        st.link_button("LinkedIn", "https://www.linkedin.com/in/francoisregis/")
        
    with right_column1:
        st.write("---")
        st.write("[Kaggle >](https://www.kaggle.com/faduregis)")
        
    with right_column2:
        st.write("---")
        st.write("[Github >](https://github.com/Regis7)")
      
