from serpapi import GoogleSearch
import os
import re
from collections import Counter
import matplotlib.pyplot as plt
import streamlit as st

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

def extract_skills(job_descriptions):
    skill_counter = Counter()
    
    for description in job_descriptions:
        words = re.findall(r'\b\w+\b', description)
        for word in words:
            # Consider words with more than 2 characters as potential skills
            if len(word) > 2:
                skill_counter[word] += 1

    return skill_counter

def plot_skills(skill_counter):
    skills, counts = zip(*skill_counter.most_common(10))
    plt.figure(figsize=(10, 6))
    plt.barh(skills, counts, color='skyblue')
    plt.xlabel('Count')
    plt.title('Top 10 Skills in Job Listings')
    plt.gca().invert_yaxis()
    plt.tight_layout()
    st.pyplot(plt)

def main():
    st.title("Jobs and needed skills")

    job_query = st.text_input("Enter job title or keyword:", "Software Engineer")
    location = st.text_input("Enter country or city name:", "Netherlands")
    num_results = 100

    if st.button("Search"):
        with st.spinner("Fetching job listings..."):
            jobs = fetch_jobs(job_query, location, num_results)
            if jobs:
                st.success(f"Found {len(jobs)} jobs")

                job_descriptions = [job['description'] for job in jobs]
                skill_counter = extract_skills(job_descriptions)

                if skill_counter:
                    st.write("### Top 10 Skills Needed")
                    plot_skills(skill_counter)
                else:
                    st.error("No skills found in the job descriptions.")
            else:
                st.error("No jobs found. Please try a different query.")

if __name__ == "__main__":
    main()
