import streamlit as st
import requests, os
from dotenv import load_dotenv

load_dotenv()
API_URL = "http://movie-env-1.eba-t9a3mau2.us-east-1.elasticbeanstalk.com"

st.set_page_config(page_title="🎬 Movie Recommender")

# --- Custom CSS --- 
st.markdown(""" 
            <p style='text-align:center; color:gray;
             font-size:13px;'> Built by <span style='color:#ff4b4b;
            '>Mehrdad Madadi🔥</span> </p> """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center; color:#ff4b4b;'>🎬 Movie Recommender System</h1>", unsafe_allow_html=True) 
st.markdown("<p style='text-align:center; color:gray;'>Similar movie discovery</p>", unsafe_allow_html=True)


st.subheader("Find Similar Movies") 
title = st.text_input("Search Movie Title") 
if title: 
        with st.spinner("Finding similar movies..."):
            res = requests.get(f"{API_URL}/similar/{title}?", timeout=15) 
            if res.status_code == 200: 
                movies = res.json() 
                if movies: 
                    cols = st.columns(5) 
                    for i, m in enumerate(movies): 
                        with cols[i % 5]: 
                            st.markdown(f""" <div class='movie-card'> <img src='{m['poster'] or "https://via.placeholder.com/150x220?text=No+Poster"}' width='150'> <p class='movie-title'>{m['title']}</p> </div> """, unsafe_allow_html=True) 
                else: st.warning("No similar movies found.") 
            else: 
                st.error(res.json().get("detail", "Unknown error."))