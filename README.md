# Movie-Recommender-System-Content-Based Web Application 🎥

Project Overview
The Movie Recommender System is a content-based filtering application that provides personalized movie recommendations based on user preferences. By analyzing genres, directors, cast, and keywords associated with movies, the system recommends films similar to the user's chosen movie. The project leverages machine learning techniques, TMDB API, and a precomputed similarity matrix to deliver accurate and efficient recommendations.

## Objectives
1. **Feature Extraction**: Identify and extract relevant features from the movie dataset, including genre, director, cast, and plot keywords.
2. **Similarity Calculation**: Implement a method to calculate the similarity between movies based on the extracted features.
3. **Recommendation Generation**: Develop an algorithm to generate movie recommendations for users based on their past preferences.
4. **Dynamic Data Integration**: Fetch real-time movie data (genres, cast, keywords) using the TMDB API.
5. **User Interface**: Create a user-friendly interface where users can input their movie preferences and receive recommendations.
6. **Personalized Recommendations**: Provide users with a curated list of movies based on their preferences.

## **Methodology / Methods**  
1. **Data Collection**:  
   - Movie dataset sourced from TMDB API and preprocessed into a structured format.  
   - Additional metadata such as genres, directors, cast, and keywords fetched dynamically using API requests.  

2. **Content-Based Filtering**:  
   - Features such as `genres`, `director`, `cast`, and `keywords` are combined into a single text-based feature vector.  
   - Cosine similarity is used to calculate the similarity between movies based on the combined features.  

3. **Precomputed Similarity Matrix**:  
   - A similarity matrix is built offline and loaded during runtime for efficient recommendations.  

4. **Web Application**:  
   - **Streamlit** is used to create an interactive interface for users to search for movies, view recommendations, and explore trending movies.

### User Interface Screenshot:
![home 1](https://github.com/user-attachments/assets/65f9920f-a94d-4861-9cc6-8aa5ce533094)

![home 2](https://github.com/user-attachments/assets/d573c357-a6c7-4fbe-8ba2-957a98ac486b)

![trending](https://github.com/user-attachments/assets/a88d9796-92c1-4b9a-ac37-945a64b3ef60)

## **Conclusion**  
The Movie Recommender System is an effective tool for discovering movies that align with a user's taste. By utilizing content-based filtering, the system provides tailored recommendations while ensuring ease of use through an intuitive interface. The integration of real-time data from the TMDB API further enhances its relevance and adaptability.

## **Future Work**  
- **Hybrid Recommendation System**: Combine content-based and collaborative filtering for more robust recommendations.  
- **User Profiling**: Add features to analyze user watch history and preferences for personalized suggestions.  
- **Advanced Visualizations**: Enhance the UI with interactive charts and data-driven insights.  

## **Contact**  
For questions or feedback, reach out to **[Muhammad Hamza](mailto:mr.hamxa942@gmail.com) or [Linkedin](https://www.linkedin.com/in/muhammad-hamza-khattak/)**.  
