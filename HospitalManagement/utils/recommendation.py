import csv
import math
import re

import inflect
import pandas as pd

from .correct_wrong_words import fix_wrong_words
from .stop_words import stop_words

df = pd.read_csv("./datasets/Training.csv")
p = inflect.engine()


columns = df.columns[:-2]


def remove_duplicate_words(sentence):
    unique_sentence = " ".join(set(sentence.split()))
    return unique_sentence


def remove_stop_words(sentence):
    new_word_list = []
    unique_sentence = remove_duplicate_words(sentence)
    print(unique_sentence)
    sentence = fix_wrong_words(unique_sentence)
    # split if the , or space is found in the sentence
    splitted_words = re.split(r"[,\s]+", sentence.strip().lower())
    for word_ in splitted_words:
        if word_ not in stop_words:
            word = p.singular_noun(word_)
            if word:
                cleaned_word = clean_numbers_and_special_characters(word)
                new_word_list.append(cleaned_word)
            else:
                new_word_list.append(
                    clean_numbers_and_special_characters(word_)
                )

    return [i for i in new_word_list if i]


def convert_to_verb1(word):
    pattern = r"ing$"
    base_verb = re.sub(pattern, "", word)
    return base_verb


def clean_numbers_and_special_characters(word):
    pattern = "[^a-zA-Z]"
    if re.match(pattern, word):
        formatted_word = re.sub(pattern, "", word)
        return formatted_word
    return word


def create_vector_from_input(formatted_input_list):
    column_list = [" ".join(col.split("_")) for col in columns]
    vector = [0] * len(column_list)

    for i in range(len(column_list)):
        for keyword in column_list[i].split():
            if keyword in formatted_input_list:
                vector[i] = 1
                # print(i)
                break
    return vector


def dot_product(vector1, vector2):
    return sum([vector1[i] * vector2[i] for i in range(len(vector1))])


def magnitude(vector):
    return math.sqrt(sum([x**2 for x in vector]))


def cosine_similarity(vector1, vector2):
    return dot_product(vector1, vector2) / (
        magnitude(vector1) * magnitude(vector2)
    )


def get_cosine_similarities(vec2):
    similarities = []
    with open("./datasets/updated_training_data.csv") as file_obj:
        reader_obj = csv.reader(file_obj)
        next(reader_obj)
        for row in reader_obj:
            int_row = [int(num) for num in row[1:]]
            result = cosine_similarity(int_row, vec2)
            similarities.append([int(row[0]), result])

    return similarities


def sort_similarities(similarities):
    sorted_scores = sorted(similarities, key=lambda x: x[1], reverse=True)
    return sorted_scores[:30]


def give_disease(input_text):
    disease_result = []
    formatted_list = remove_stop_words(input_text)
    vec2 = create_vector_from_input(formatted_list)
    if all(val == 0 for val in vec2):
        return None
    # print(vec2)
    similarities = get_cosine_similarities(vec2)
    results = sort_similarities(similarities)
    for res in results:
        disease_result.append(df.iloc[res[0]]["prognosis"])
    return list(set(disease_result))


if __name__ == "__main__":
    input_text = input("Enter your symptoms: ")
    res = give_disease(input_text)
    print(res)
