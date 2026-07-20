import time
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1. BUILT-IN MOVIE DATASET (Sample movies dataset with genres & plot tags)
movies_data = {
    'Movie_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Title': [
        'Inception',
        'The Dark Knight',
        'Interstellar',
        'The Matrix',
        'The Avengers',
        'The Notebook',
        'La La Land',
        'The Hangover',
        'Superbad',
        'Toy Story'
    ],
    'Genre_and_Plot': [
        'Sci-Fi Action Thriller mind-bending dreams reality heist Christopher Nolan',
        'Action Crime Drama superhero Batman dark city Gotham hero superhero',
        'Sci-Fi Adventure Drama space exploration black hole time travel Christopher Nolan',
        'Sci-Fi Action virtual reality simulation future machine rebellion cyberpunk',
        'Action Sci-Fi Superhero Marvel team aliens save world fight',
        'Romance Drama love story relationship emotional classic couple',
        'Romance Drama Music musical jazz romance Los Angeles dreams relationship',
        'Comedy Las Vegas bachelor party funny friends chaotic night missing person',
        'Comedy high school teen friends party awkward funny high school',
        'Animation Adventure Comedy family toys come alive friendship kids'
    ]
}

# Converting dictionary to Pandas DataFrame
df = pd.DataFrame(movies_data)

# 2. FEATURE EXTRACTION (TF-IDF Vectorizer)
# Text descriptors ko numerical vectors (mathematical scores) mein badalna
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['Genre_and_Plot'])

# 3. COSINE SIMILARITY (Similarity matrix calculate karna)
# Har movie ka doosri har movie ke sath similarity percentage nikalna
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)


# 4. RECOMMENDATION ENGINE FUNCTION
def get_recommendations(movie_title, top_n=3):
    movie_title_lower = movie_title.lower().strip()

    # Matching movie index in our DataFrame
    matching_movies = df[df['Title'].str.lower() == movie_title_lower]

    if matching_movies.empty:
        return None

    # Select index of input movie
    idx = matching_movies.index[0]

    # Calculate similarity scores for all movies against the selected movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort movies based on similarity scores in descending order
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Exclude the movie itself (index 0) and pick top_n recommendations
    sim_scores = sim_scores[1:top_n + 1]

    # Fetch recommended movie indices and titles
    movie_indices = [i[0] for i in sim_scores]
    return df['Title'].iloc[movie_indices].tolist()


# --- MAIN INTERACTIVE INTERFACE ---
print("🎬 ================================================= 🎬")
print("    WELCOME TO THE MOVIE RECOMMENDATION SYSTEM      ")
print("🎬 ================================================= 🎬\n")

print("Available movies in database:")
for title in df['Title']:
    print(f" • {title}")

while True:
    print("\n" + "-" * 50)
    user_movie = input("Enter a movie name from the list above (or type 'exit'): ").strip()

    if user_movie.lower() == 'exit':
        print("\n🎉 Congratulations! All 4 Internship Tasks Completed successfully!")
        break

    if not user_movie:
        continue

    print("\n🔍 Analyzing genres, plot tags, and keywords...")
    time.sleep(1)  # Human-made pause effect

    recommendations = get_recommendations(user_movie, top_n=3)

    if recommendations is None:
        print("❌ Movie not found in database! Please pick a movie from the list above.")
    else:
        print(f"\n🍿 Because you liked '{user_movie}', you might also enjoy:")
        for idx, rec in enumerate(recommendations, 1):
            print(f"  {idx}. {rec}")