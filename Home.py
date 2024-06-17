# Modules
import requests
import streamlit as st
import os
from streamlit_lottie import st_lottie
from PIL import Image
import streamlit.components.v1 as components
import pandas as pd
import numpy as np


# ----- PAGE CONFIGURATION ---
st.set_page_config(page_title="faduregis", page_icon=":🛠:", layout = "wide")

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()  


with st.container():
    st.title(" 🛠 FaduRegis' palyground")
   #st.subheader("FaduRegis")
    st.write(""" 
FaduRegis is your premier hub for hands-on learning and experimentation in technology, coding, data analytics, and data science. Whether you're a novice or a seasoned developer, our platform provides a comprehensive array of tools and resources to enhance your skills and transform your ideas into reality.

""")
    
# Initialize the visitor count
if not os.path.exists('visitor_count.txt'):
    with open('visitor_count.txt', 'w') as f:
        f.write('0')

# Read the current visitor count
with open('visitor_count.txt', 'r+') as f:
    count = int(f.read()) + 1
    f.seek(0)
    f.write(str(count))
    f.truncate()

# Streamlit app
st.write(f"You are visitor number: {count} welcome back soon!")


from serpapi import GoogleSearch

# Set your SerpApi API key
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY", "5756fbdfdafb0ac6ea4d29e6aba9245e20e833ba78959b766e205471662bf930")

def fetch_jobs(query, location, num_results=100):
    params = {
        "engine": "google_jobs",
        "q": query,
        "location": location,
        "api_key": SERPAPI_API_KEY,
        "num": num_results
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    return results.get("jobs_results", [])

def main():
    st.title("Search for jobs in the Netherlands")
    st.subheader("! The app is still under development to ensure everything is fine!")

    job_query = st.text_input("Enter job title or keyword:", "Software Engineer")
    location = "Netherlands"
    num_results = 100

    if st.button("Search"):
        with st.spinner("Fetching job listings..."):
            jobs = fetch_jobs(job_query, location, num_results)
            if jobs:
                st.success(f"Found {len(jobs)} jobs")
                for idx, job in enumerate(jobs, start=1):
                    st.write(f"### {idx}. {job['title']}")
                    st.write(f"**Company**: {job['company_name']}")
                    st.write(f"**Location**: {job['location']}")
                    st.write(f"**Posted at**: {job['detected_extensions']})")
                    st.write(f"**Links**: {job['related_links']})")
                    st.write(f"**Description**: {job['description'][:200]}...")  # Show a snippet of the description
                    st.write("---")
            else:
                st.error("No jobs found. Please try a different query.")

if __name__ == "__main__":
    main()



#############################################################

# --- COPY RIGHTS --

with st.container():
    left_column1, left_column2, right_column1, right_column2 = st.columns(4)
    with left_column1:
        st.write("---")
        st.write("@ faduregis 2024")
    
    with left_column2:
        st.write("---")
        st.write("[LinkedIn >](https://www.linkedin.com/in/francoisregis/)")
        
    with right_column1:
        st.write("---")
        st.write("[Kaggle >](https://www.kaggle.com/faduregis)")
        
    with right_column2:
        st.write("---")
        st.write("[Github >](https://github.com/Regis7)")
      
