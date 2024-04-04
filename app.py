import streamlit as st
import pandas as pd
import requests
import pickle
# import joblib
import bz2file as bz2

def decompress_pickle(file):
    data = bz2.BZ2File(file, 'rb')
    data = pickle.load(data)
    return data




# movie_list = pickle.load(open("movies.pkl", "rb"))
# movie_list = joblib.load("movies2")
movie_list =  decompress_pickle(r"moviecom.pbz2")
movies_list = movie_list["title"].values
st.title('Movie Recommend System')

selected_movie_name = st.selectbox('Select a Movie', movies_list)

# similarity = pickle.load(open("similarity.pkl", "rb"))
# similarity = joblib.load("similarity2")
def fetch_poster(mId):
    url = f"https://api.themoviedb.org/3/movie/{mId}?api_key=14cb3aa18123646d9ea2c4ac6100dab7&language=en-US"
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(movie):
    movie_index = movie_list[movie_list["title"] == movie].index
    similarity = decompress_pickle(r"similarityCom.pbz2")
    distances = similarity[movie_index]
    movie_listt = sorted(
        list(enumerate(distances[0])), reverse=True, key=lambda x: x[1])[1:11]
    recommended_movies = []
    recommended_movies_posters = []
    for i in movie_listt:
        movie_id = movie_list.iloc[i[0]]["id"]
        # recommended_movies_posters.append(fetch_poster(movie_id))
        recommended_movies.append(movie_list.iloc[i[0]]["title"])
    return recommended_movies, recommended_movies_posters


st.write('You selected:', selected_movie_name)
if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)
    
    col1, col2, col3, col4, col5=st.columns(5)
    col6, col7, col8, col9, col10 = st.columns(5)

    with col1:
        st.text(names[0])
       # st.image(posters[0])

    with col2:
        st.text(names[1])
       # st.image(posters[1])

    with col3:
        st.text(names[2])
       # st.image(posters[2])
    with col4:
        st.text(names[3])
       # st.image(posters[3])

    with col5:
        st.text(names[4])
      #  st.image(posters[4])
    with col6:
        st.text(names[5])
       # st.image(posters[5])

    with col7:
        st.text(names[6])
        # st.image(posters[6])

    with col8:
        st.text(names[7])
        # st.image(posters[7])
    with col9:
        st.text(names[8])
       # st.image(posters[8])

    with col10:
        st.text(names[9])
       # st.image(posters[9])



hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)
