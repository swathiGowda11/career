import streamlit as st
import pandas as pd

st.title("Career Guidance AI")

# Navigation
page = st.sidebar.radio("Navigate", ["Jobs", "Skills", "Courses", "Scholarships"])

if page == "Jobs":
    st.header("Job Opportunities")
    st.text_input("Search Jobs")
    st.selectbox("Location", ["All", "NY", "CA", "Remote"])
    st.dataframe(pd.DataFrame({
        "Job": ["Data Analyst", "ML Engineer"],
        "Company": ["ABC Inc", "XYZ Corp"],
        "Location": ["NY", "Remote"]
    }))

elif page == "Skills":
    st.header("Skill Recommendations")
    st.multiselect("Select Skills", ["Python", "Data Analysis", "Machine Learning"])

elif page == "Courses":
    st.header("Recommended Courses")
    st.radio("Level", ["Beginner", "Intermediate", "Advanced"])
    st.write("Course 1: Learn Python Basics")

elif page == "Scholarships":
    st.header("Scholarships")
    st.dataframe(pd.DataFrame({
        "Name": ["AI Scholarship", "Data Science Grant"],
        "Eligibility": ["Students", "Open to All"],
        "Link": ["https://...", "https://..."]
    }))
