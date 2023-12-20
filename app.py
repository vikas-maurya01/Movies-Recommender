import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    index = movies[movies['title']==movie].index[0]
    distances = similarity[index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    for i in movies_list:
        movie_id = i[0]
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies
movies_dict= pickle.load(open('movies_dict.pkl','rb'))
movies =pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))
st.title('Movies Recommender System')
option = st.selectbox('Which movie do you like best?',movies['title'].values)

if st.button('Recommend'):
    reco_movies = recommend(option)
    for i in reco_movies:
        st.write(i)
      