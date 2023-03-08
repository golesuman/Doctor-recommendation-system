import re

import spacy

nlp = spacy.load("en_core_web_md")  # Load the medium-sized English language model

import pandas as pd

columns = pd.read_csv("/home/suman/Desktop/Doctor-recommendation-system/HospitalManagement/datasets/updated_training_data.csv").columns[1:]

new_columns = [" ".join(re.split("_", column)) for column in columns]
# Create a dictionary to store the similarity scores between the input text and each column
similarity_scores = {}

# Define the input text
# input_text = "i have extreme pain in the chest and also have stomach bleeding. And My eyes are also red."

# Process the input text with spaCy
def create_vector_based_on_similar_word(input_text):
    doc = nlp(input_text)

    # Iterate over each column and calculate its similarity score with the input text
    for column in new_columns:
        column_text = nlp(column)
        similarity_score = doc.similarity(column_text)
        similarity_scores[column] = similarity_score

    # Create the vector by mapping the similarity scores to 1 or 0 based on a threshold value
    threshold = 0.5 # Adjust this value based on your needs
    vector = [1 if similarity_scores[column] >= threshold else 0 for column in new_columns]
    return vector
    # for key, value in similarity_scores.items():
    #     if value > 0.65:
    #         print(key, value)

# print(similarity_scores)
# print(vector)