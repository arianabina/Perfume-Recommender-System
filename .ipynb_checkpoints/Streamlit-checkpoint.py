import pandas as pd
import numpy as np
import streamlit as st
from sklearn.metrics import euclidean_distances
from sklearn.feature_extraction.text import TfidfVectorizer


# Load the data
df1 = pd.read_csv('Data/fivek_subset_data.csv')

# Convert 'main_accords' column to strings
df1['main_accords'] = df1['main_accords'].astype(str)

# Extract unique individual accords
unique_accords = set()
for accords in df1['main_accords'].str.split(', '):
    if isinstance(accords, list):  # Check if accords is a list
        unique_accords.update(accords)

# Sort unique accords alphabetically
unique_accords = sorted(list(unique_accords))

#Function to Recommend Perfumes based on Euclidian Distance
def recommend_perfumes(selected_accords, df):
    # Convert selected accords into a string
    selected_accords_str = ', '.join(selected_accords)

    #Compute TF-IDF vectors for the selected accords and perfumes' accords
    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(list(df['main_accords']) + [selected_accords_str])

    # Compute Euclidean distances between the selected accords and perfumes' accords
    euclidean_dist = euclidean_distances(tfidf_matrix[-1], tfidf_matrix[:-1])

    # Get indices of perfumes sorted by Euclidean distances
    dist_indices = euclidean_dist.argsort()[0]

    # Filtered indices excluding the selected accords
    filtered_indices = [i for i in dist_indices if i != len(df) - 1]

    # Recommend up to five perfumes based on the filtered indices
    recommendations = df.iloc[filtered_indices[:5]][['brand', 'perfume', 'notes']]
    return recommendations
    

# Custom CSS to set theme colors and font
custom_css = """
<style>
body {
    background-color: #d3d6f7; /* Light blue-gray background */
    color: #090c0b; /* Dark gray text color */
    font-family: serif; /* Serif font */
}
</style>
"""

# Streamlit app
def main():
    # Inject custom CSS to set theme
    st.markdown(custom_css, unsafe_allow_html=True)

    st.title('Fragrance Finder')

    # Inserting the image without a caption
    st.image('Images/fragrance.png', use_column_width=True)

    st.sidebar.title('How Do You Want To Smell?')

    # Dropdown menu for selecting accords
    selected_accords = st.sidebar.multiselect('Select up to three accords', unique_accords, [], key='accords')
    
    if len(selected_accords) > 3:
        st.sidebar.error("Please select up to three accords.")
        return
    
    if st.sidebar.button('Get Recommendations'):
        recommendations = recommend_perfumes(selected_accords, df1)
        st.subheader('Recommended Perfumes')

        # Check if recommendations is not empty
        if not recommendations.empty:
            recommendations.reset_index(drop=True, inplace=True)  # Resetting index
            recommendations.index += 1  # Start numbering from 1
            st.table(recommendations)  # Display table with recommendations
        else:
            st.error("Sorry! We can't find any perfumes that match the selected accords. Please try again.")

# Run the Streamlit app
if __name__ == '__main__':
    main()
