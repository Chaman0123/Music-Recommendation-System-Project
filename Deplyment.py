import streamlit as st
import pickle
import pandas as pd

def recommend(song):
    song_index = songs[songs['album_name'] == song].index[0]
    distances = similarity[song_index]
    song_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_songs = []
    for i in song_list:
        recommended_songs.append(songs.iloc[i[0]].album_name)
    return recommended_songs

song_dict = pickle.load(open(r"C:\Users\prash\Downloads\songs_dict.pkl",'rb'))
songs = pd.DataFrame(song_dict)

similarity = pickle.load(open(r"C:\Users\prash\Downloads\similarity.pkl",'rb'))

st.title('Song Recommendation System')

selected_song_name = st.selectbox(
    'How would you like to be contacted?',
    songs['album_name'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_song_name)
    for i in recommendations:
        st.write(i)




