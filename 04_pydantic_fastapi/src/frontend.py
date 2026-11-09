import streamlit as st
import requests
import pandas as pd


def display_movies():
    movie_str = st.text_input("Give a statement and it will give back a movie")

    if movie_str:
        movie = requests.post(f"http://127.0.0.1:8000/movie",
                              json={"prompt": movie_str}).json()
        st.write(movie)

    genre = st.selectbox("Choose genre", options=[
                         "action", "comedy", "cartoon"])

    movies = requests.get(
        f"http://127.0.0.1:8000/movies?genre={genre}").json()

    st.dataframe(pd.DataFrame(movies))


def layout():
    st.markdown("# Movies")
    display_movies()


if __name__ == '__main__':

    layout()
