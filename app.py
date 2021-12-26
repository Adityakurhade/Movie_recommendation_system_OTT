# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 12:19:01 2021

@author: Adi Kurhade
"""

import pickle
import streamlit as st
import pandas as pd

movies = pickle.load(open("original_df.pkl","rb"))
similarity = pickle.load(open("similarity.pkl",'rb'))
#data = pickle.load(open("newdf.pkl","rb"))

st.header("Movie/TV show Recommendaion System")

st.write('''This recommendation system will recommend you movies or Tv shows
         to watch from three popular OTT platforms viz:
             Netflix, Amazon Prime, Disney+Hotstar''')

movie_list = movies['title']
selected_movie = st.selectbox("Type or select Movie/TV show from list",
                              movie_list)

def recommend(movie):
    index = movies[movies['title']== movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True,key=lambda x:x[1])
    dic={0:movies.iloc[distances[1][0]],
         1:movies.iloc[distances[2][0]],
         2:movies.iloc[distances[3][0]],
         3:movies.iloc[distances[4][0]],
         4:movies.iloc[distances[5][0]]}
    df = pd.DataFrame(dic).T
    return df

if st.button("Show Recommendation"):
    st.write("Following are some movies/ TV shows you can watch")
    st.table(data=recommend(selected_movie))