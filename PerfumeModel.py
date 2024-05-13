import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the data
df = pd.read_csv('/Users/aribina/Documents/Projects/Project 5/clean_perfume_data.csv')

# Vectorize the notes column
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df['notes'].values.astype('U'))

# Compute the cosine similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Function to recommend perfumes based on user input
def recommend_perfumes(perfume_name, cosine_sim=cosine_sim, df=df):
    idx = df[df['perfume'] == perfume_name].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]  # Top 10 similar perfumes
    perfume_indices = [i[0] for i in sim_scores]
    return df['perfume'].iloc[perfume_indices]

# Streamlit app
def main():
    st.title('Fragrance Recommender System')
    st.sidebar.title('User Input')

    # User input
    perfume_name = st.sidebar.text_input('Enter a perfume name') 
    if st.sidebar.button('Get Recommendations'):
        recommendations = recommend_perfumes(perfume_name)
        st.subheader('Recommended Perfumes')
        st.write(recommendations)

if __name__ == '__main__':
    main()