# <center> Fragrance Recommender System </center>
![banner](Images/OrangeBanner.png)

### Overview
---
Welcome to the Fragrance Recommender System! This project is designed to help users discover new perfumes based on their preferred scent profiles. By leveraging a recommendation algorithm based on euclidian distance, the engine suggests fragrances that match the user's specified perfume accords, making it easier for users to find scents they will love.

### Data Dictionary
---
| Feature     | Type     | Description             |
|-------------|----------|-------------------------|
| brand   | string   | The brand or maker of a perfume|
| perfume   | string   | The name of a particular perfume|
| launch_year   | integer   | The year a perfume was released|
| main_accords   | string   | The fragrance family(s) that a perfume belongs to; Example: Floral|
| notes   | string   | The specific notes in a fragrance; Example: Rose |



### Executive Summary
---
The objectives of this project are as follows:

1. Input Collection: Users enter their preferred perfume accords they want in a fragrance. 
2. Feature Extraction: The system processes the input and extracts perfumes corresponding to the specified accords.
3. Similarity Calculation: Using Euclidian Distance, the system calculates the similarity between the user's input and each perfume in the database.
4. Recommendation Generation: The top 5 most similar perfumes are selected and presented as recommendations to the user. 

Data Source:
* https://www.kaggle.com/datasets/nandin1999/perfume-recommendation-dataset


### Data Overview 
---
After cleaning, the dataset contained: 
* 144 fragrance families
* 1,302 notes
* 2,536 unique brands
* 33,146 unique perfumes


### Model Optimization & Evauluation 
---
I created 3 recommendation models in total: 
* A baseline model that recommends perfumes randomly
* A model that recommends based on Cosine Similarty
* A model that recommends based on Euclidian Distance

I compared these three models against eachother by choosing the accord "wine" and comparing the perfumes that each recommender ouput. 
* The Euclidian Distance model and the Cosine Similrity model recommended the exact same perfumes, albeit in a slightly different order.
* The Random Recommender model did not recommend any relevant perfumes containing the specified "wine" accord.
* In the end, I chose to use the Euclidian Distance model because I found it to be less computationally intensive and had a faster run time.

### Model Deployment & Demo
* I am using streamlit to deploy my model.
* Here, the user can choose up to three fragrance accords that they wish to find in a perfume.
* Then, they will be shown 5 fragrances that are similar, including the perfume name, brand, and the notes within each fragrance.
* For a faster runtime, I am only using a small subset of 5,000 perfumes to deploy on streamlit.
* Therefore, the recommendations given are somewhat limited, when compared to utilizing the full dataset of over thirty thousand perfumes. 