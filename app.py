import pandas as pd
import streamlit as st
import pickle
import requests
from streamlit_option_menu import option_menu

# Function to fetch movie poster
def fetch_poster(movie_id):
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=1d104ae386227827ab615b80ac7ceaed&language=en-US'
    )
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data.get("poster_path", "")

# Function to fetch additional movie details
def fetch_movie_details(movie_id):
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=1d104ae386227827ab615b80ac7ceaed&language=en-US'
    )
    data = response.json()
    return {
        "overview": data.get("overview", "No overview available."),
        "release_date": data.get("release_date", "Unknown"),
        "rating": data.get("vote_average", "N/A"),
    }

# Recommendation function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    movie_details = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
        movie_details.append(fetch_movie_details(movie_id))

    return recommended_movies, recommended_movies_posters, movie_details

# Load models
movies_dict = pickle.load(open("model/movies_dict.pkl", 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open("model/similarity.pkl", 'rb'))

# Streamlit UI
st.title("🎥 Movie Recommender System (Content-Based Filter)")
st.markdown("---")

# Sidebar navigation
with st.sidebar:
    selected = option_menu(
        "Navigation",
        ["Home", "Trending", "About"],
        icons=["house", "fire", "info-circle"],
        menu_icon="menu-app",
        default_index=0,
    )

# Main section
if selected == "Home":
    st.header("Get Recommendations for Your Favorite Movie 🍿")
    selected_movie_name = st.selectbox("Search for a movie", movies['title'].values)

    if st.button("Recommend"):
        with st.spinner("Fetching recommendations..."):
            names, posters, details = recommend(selected_movie_name)

        st.subheader("Recommended Movies 🎬")

        for name, poster, detail in zip(names, posters, details):
            # Display a detailed card for each movie
            st.markdown("### " + name)
            cols = st.columns([1, 2])  # Create columns for poster and details
            with cols[0]:
                st.image(poster, use_container_width=True)
            with cols[1]:
                st.markdown(f"**Release Date:** {detail['release_date']}")
                st.markdown(f"**Rating:** {detail['rating']}")
                st.markdown("**Overview:**")
                st.write(detail["overview"])
            st.markdown("---")  # Add a separator between movies

elif selected == "Trending":
    st.header("🔥 Trending Movies")
    st.write("Fetching the latest popular movies...")

    # Fetch trending movies from TMDB
    response = requests.get(
        'https://api.themoviedb.org/3/trending/movie/day?api_key=1d104ae386227827ab615b80ac7ceaed'
    )
    trending_data = response.json().get("results", [])

    for movie in trending_data[:8]:  # Show top 8 trending movies
        st.markdown("### " + movie.get("title", "Unknown"))
        cols = st.columns([1, 2])  # Create columns for poster and details
        with cols[0]:
            st.image(f"https://image.tmdb.org/t/p/w500/{movie.get('poster_path', '')}", use_container_width=True)
        with cols[1]:
            st.markdown(f"**Release Date:** {movie.get('release_date', 'Unknown')}")
            st.markdown(f"**Rating:** {movie.get('vote_average', 'N/A')}")
            st.markdown("**Overview:**")
            st.write(movie.get("overview", "No overview available."))
        st.markdown("---")  # Add a separator between movies

elif selected == "About":
    st.header("About 🎥 Movie Recommender")
    st.write(
        """
        This Movie Recommender System is built using **Streamlit** and **TMDB API**. 
        It provides personalized movie recommendations and displays trending movies. 
        Explore and find your next favorite movie!
        """
    )
    st.markdown("---")
    st.write("Created ❤️ by Muhammad Hamza")
