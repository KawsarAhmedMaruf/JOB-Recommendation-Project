import streamlit as st
import pandas as pd
import pickle
from streamlit.components.v1 import html

# Load data from pickle files
with open('df8.pkl', 'rb') as file:
    df = pd.read_pickle(file)

with open('similarity8.pkl', 'rb') as file:
    similarity = pd.read_pickle(file)


# Function to generate job recommendations
def recommendation(title):
    idx = df[df['Title'] == title].index[0]
    idx = df.index.get_loc(idx)
    distances = sorted(list(enumerate(similarity[idx])), key=lambda x: x[1], reverse=True)[1:21]
    
    jobs = []
    for i in distances:
        jobs.append(df.iloc[i[0]].Title)
        
    return jobs


# Streamlit app
st.title('Job Recommendation System')
title = st.selectbox('Search job', df['Title'])

if st.button('Get Recommendations'):
    jobs = recommendation(title)
    
    if jobs:
        st.subheader('These are the top recommended jobs for you:')
        for job in jobs:
            html(f"<div style='border: 1px solid gray; padding: 0.5rem; margin-bottom: 2px;'>{job}</div>")
    else:
        st.write('No recommendations found')