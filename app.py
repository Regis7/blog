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
img_process_view = Image.open("images/process view.png")


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
            - As the solutions architect, I'm part of an entrepreneurial-spirited organization, and in charge of designing the roadmap to (re)solve architectural issues, unifying data flows, and driving organizational impact.
            - I bring oversight, analysis, and recommendations for the way various systems/tools (e.g., the financial system, the contracting and procurement system etc.) are (or could be) integrated, build the roadmap to deliver on the IT department’s vision, and lead the execution of a fit-for-purpose data flow architecture.
            """
        )
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
        st.write("##")
        st.write("##")
        st.image(img_process_view)
    with text_column:
        st.subheader("Currently running and ongoing projects:")
        st.write("FADU Techs company")
        st.write(
             """
            - FADU Techs is an emerging mobile and web application development, data and web hosting company in Rwanda. 
            - I am a co-founder of Fadu Techs. Through FADU Techs, I have got the exposure and experience to work with different sectors by offering IT-based solutions and breaking down complex and technical topics for stakeholders to understand as well as heading the analytics department.
            """
        )
        st.write("[Read more >](https://fadu.co.rw/)")
        st.write("##")
        st.write("SAD(Solution architecture document)")
        st.write("A solution architecture document outlines the high-level design and structure of a proposed solution to address a specific business problem or technical challenge. It serves as a blueprint for development teams and stakeholders, providing a clear understanding of how different components will interact to achieve the desired outcomes.")
        st.write("As most of you requested, I have developed a solution architecture document to assist whoever needs a SAD template. This document has a business view, process view, non-functional requirements, conceptual view, solution view, data view, security view, and integration view.")
        st.write("[Read more >](#)")
        
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
        st.write("Connecting is key in our digital age. Reach out and let's chat! Whether you have questions, ideas, or just want to say hi, don't hesitate to get in touch with me. Communication bridges gaps and fosters understanding. Feel free to drop a message – I'm here to listen and engage.")
        st.lottie(lottie_coding, height=350, key="coding")
        
# --- COPY RIGHTS --

with st.container():
    left_column1, left_column2, right_column1, right_column2 = st.columns(4)
    with left_column1:
        st.write("---")
        st.write("@ Regis 2023")
    
    with left_column2:
        st.write("---")
        st.write("[LinkedIn >](https://www.linkedin.com/in/francoisregis/)")
        
    with right_column1:
        st.write("---")
        st.write("[Kaggle >](https://www.kaggle.com/faduregis)")
        
    with right_column2:
        st.write("---")
        st.write("[Github >](https://github.com/Regis7)")
      
    