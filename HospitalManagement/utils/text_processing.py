import re

import inflect
import pandas as pd
from spellchecker import SpellChecker
from utils.cosine_similarity import get_cosine_similarities

from .stop_words import stop_words

df = pd.read_csv("./datasets/updated_randomized_dataset.csv")

p = inflect.engine()
spell = SpellChecker()

columns = df.columns[:-2]


def remove_duplicate_words(sentence):
    unique_sentence = " ".join(set(sentence.split()))
    return unique_sentence


def remove_stop_words(sentence):
    new_word_list = []
    unique_sentence = remove_duplicate_words(sentence)
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
                    clean_numbers_and_special_characters(word_))
    return [i for i in new_word_list if i]


def convert_to_verb1(word):
    pattern = r"ing$"
    base_verb = re.sub(pattern, "", word)
    return base_verb


def clean_numbers_and_special_characters(word):
    pattern = r"[^a-zA-Z]"
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


def sort_similarities(similarities):
    sorted_scores = sorted(similarities, key=lambda x: x[1], reverse=True)
    return sorted_scores


def give_disease(input_text):
    disease_result = []
    formatted_list = remove_stop_words(input_text)
    print(formatted_list)
    vec2 = create_vector_from_input(formatted_list)
    if all(val == 0 for val in vec2):
        return None
    # print(vec2)
    similarities = get_cosine_similarities(vec2)
    results = sort_similarities(similarities)
    print(results)
    for res in results:
        if res[1] > 0.2:
            disease_result.append(df.iloc[res[0]]["prognosis"])
    return list(set(disease_result))


def is_input_valid(input_text):
    pattern = r"[a-zA-Z]+"
    bool_value = re.match(pattern, input_text)
    return bool_value



def fix_wrong_words(text):
    corrected_sentence = []
    for word in text.split():
        if word:
            corrected_sentence.append(spell.correction(word))
    new_fixed_text = " ".join(corrected_sentence)
    return new_fixed_text



def remove_special_characters_from_word(word):
    pattern = r"[^a-zA-Z]"
    words = re.split(pattern, word)
    return words



if __name__ == "__main__":
    input_text = input("Enter your symptoms: ")
    res = give_disease(input_text)
    print(res)
