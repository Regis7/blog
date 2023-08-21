import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
#from streamlit-option-menu import option-menu

#st.title("Stream Option menu")

# ---- Emojes: https://www.webfx.com/tools/emoji-cheat-sheet/ 

st.set_page_config(page_title="Blog", page_icon=":tada:", layout = "wide")

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
img_contact_form = Image.open("images/FaduTech_Logo.png")


# ---- HEADER SECTION ----

with st.container():
    st.subheader("Hello, I'm Regis :🤝:")
    st.title("An IT solutions architect")
    st.write("I have been in the tech field since I started university in 2009. I did Computer Science for my bachelor's degree and a master's degree in Information Systems, specializing in AI and Big Data Analytics at Uppsala University in Sweden. In these 10+ years, I worked as a web developer, webmaster, tech consultant, data analyst, and now as an IT solutions architect.")
    st.write("[Read more >](https://www.linkedin.com/in/francoisregis/)")
    
# --- WHAT I DO ---
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("#")
        st.write(
            """
            - As an IT solutions architect, my primary responsibility is to design and oversee the implementation of effective, scalable, and secure IT solutions that align with organization's business goals.
            - I collect, process, and interpret large datasets to extract valuable insights and inform data-driven decision-making for organizations.
            -  I design, develop, and deploy complex machine learning models and systems to solve real-world problems and optimize algorithm performance for various applications.
            - 
            """
        )
        st.write("[Read more >](#)")
    with right_column:
        st.lottie(lottie_analytics, height=300, key="analytics")
        
# ---- PROJECT ---

with st.container():
    st.write("---")
    st.header("My projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        # insert image
        st.image(img_contact_form)
    with text_column:
        st.subheader("Currently running and ongoing projects:")
        st.write(
             """
            - FADU Techs is an emerging mobile and web application development, data and web hosting company in Rwanda. 
            - I am a co-founder of Fadu Techs. Through FADU Techs, I have got the exposure and experience to work with different sectors by offering IT-based solutions and breaking down complex and technical topics for stakeholders to understand as well as heading the analytics department.
            - 
            """
        )
        
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
        # -- st.empty()
        st.lottie(lottie_coding, height=450, key="coding")
        
# --- COPY RIGHTS --

with st.container():
    st.write("---")
    st.write("@ Regis 2023")
      
    