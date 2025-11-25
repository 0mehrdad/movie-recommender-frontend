# 🎬 Movie Recommender – Streamlit Frontend

A lightweight Streamlit frontend for a movie recommendation system powered by a FastAPI backend.

🔗 **Live App:**  
https://movie-recommender-frontend-bx3xdouaxpshlaeiw5b4rk.streamlit.app/

---

## 🧠 About the Project
This app lets users search for a movie and instantly get back the **top 5 most similar movies**.  
The backend handles all recommendation logic (MovieLens 32M dataset + OpenAI embeddings).  
This repo only contains the **frontend UI**.

---

## 🖥️ Features
- Search for any movie title  
- Displays 5 similar movies with posters  
- Clean, fast Streamlit interface  
- Connects to a FastAPI backend on AWS Elastic Beanstalk  

---

## 📡 How It Works
1. User enters a movie title  
2. Frontend sends request to:
3. Backend returns list of movie titles + poster URLs  
4. UI shows them in a responsive 5-column layout  

---

## 📂 Frontend Code (Main File)

`streamlit_app.py`:

```python
import streamlit as st
import requests, os

API_URL = "http://movie-env-1.eba-t9a3mau2.us-east-1.elasticbeanstalk.com"

st.set_page_config(page_title="🎬 Movie Recommender")
...
(Full code is included in the repo.)

▶️ Run Locally
1. Install dependencies
pip install streamlit requests

2. Start the app
streamlit run streamlit_app.py

🔗 Related Repositories
Full Local Setup (Frontend + Backend): (https://github.com/0mehrdad/Movie-recommender-ML-32)

👨‍💻 Built by Mehrdad Madadi
