import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
import streamlit.components.v1 as components

#from streamlit-option-menu import option-menu

#st.title("Stream Option menu")

# ---- Emojes: https://www.webfx.com/tools/emoji-cheat-sheet/ 

# ----- PAGE CONFIGURATION ---
st.set_page_config(page_title="faduregis", page_icon=":🛠:", layout = "wide")

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()  


# --- USE LOCAL CSS

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
        
local_css("style/style.css")    

# --- LOAD ASSETS ---

# ---- Link to animation: https://lottiefiles.com/search?q=coding&category=animations 

# --- lottie_analytics = load_lottieurl("https://lottie.host/d223bd82-43fc-43f9-996c-ac1c65a9381e/zQU2WXFqOY.json")
lottie_analytics = load_lottieurl("https://lottie.host/7a9c3119-35c2-4ccc-9e6f-44331990cc2c/BVgrTYAO8L.json")
lottie_coding =load_lottieurl("https://lottie.host/9d7e5e15-25dc-445c-b71b-8683f4105d12/PswDRysQJQ.json")

# ---- HEADER SECTION ----
# components.html("""
# <div>
# <style>
# h1.heading{
#     text.align:center;
# }                
# </style>
# <h1 class="heading">
# About me
# </h1>
# <p>
# The Tech industry is constantly changing. My main focus is keeping up to date with the latest and most effective technologies. I believe in the power of people working agilely and that the data is behind the business's success.
# </p>
# </div>
# """, scrolling=True)

with st.container():
    st.subheader("Hello, I'm Regis :🤝: the tech Enthusiast")
    st.title("About")
    st.write(""" 

I am Francois Regis Dusengimana a developer and analyst behind faduregis platform. The Tech industry is constantly changing. My main focus is keeping up to date with the latest and most effective technologies. I believe in the power of people working agilely and that the data is behind the business's success.

I have been in the tech field since I started university in 2009. I did Computer Science for my bachelor's degree and a master's degree in Information Systems, specializing in AI and Big Data Analytics at Uppsala University in Sweden. I have held several positions in Rwanda, Sweden, and The Netherlands, where I closely engaged with research institutions, development actors and the private sector to foster digitalization and approaches to sustainable development challenges. My passion for digital transformation drives my quest for institutional transformation.

As co-founder of an IT service company, FADU Tech, through this company, I have the exposure and experience to work with different sectors by offering IT-based solutions and breaking down complex and technical topics for stakeholders to understand.""")
    #st.write("[Read more >](https://www.linkedin.com/in/francoisregis/)")
    st.link_button("Read more", "https://www.linkedin.com/in/francoisregis/")
    
# --- WHY THIS APP ---
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Why this App?")
        st.write("#")
        st.write(
            """
            - This application acts as a playground for me to construct and test data pipelines.
            - At the same time, it serves as a source of real-time information for our visitors.
            """
        )
    with right_column:
        st.lottie(lottie_analytics, height=250, key="analytics")
        
# ---- CONTACT FORM --- using https://formsubmit.co/

with st.container():
    st.write("---")
    st.header("Get in touch with me!")
    st.write("##")
    
    contact_form = """
    <form action="https://formsubmit.co/faduregis@gmail.com" method="POST">
         <input type="hidden" name="_captcha" value="false">
         <input type="text" name="name" placeholder= "Your name" required>
         <input type="email" name="email" placeholder = "Your email" required>
         <textarea name="message" placeholder = "Your message here" required> </textarea>
         <button type="submit">Send</button>
    </form>
     """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
        st.write("Connecting is key in our digital age. Reach out and let's chat! Whether you have questions, ideas, or just want to say hi, don't hesitate to get in touch with me. Communication bridges gaps and fosters understanding. Feel free to drop a message – I'm here to listen and engage.")
        st.lottie(lottie_coding, height=300, key="coding")
        
# --- COPY RIGHTS --

with st.container():
    left_column1, left_column2, right_column1, right_column2, right_column3 = st.columns(5)
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

    with right_column3:
        st.write("---")
        st.write("[Instagram >](https://www.instagram.com/fadu.regis/)")
      
