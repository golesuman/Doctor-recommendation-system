import re
import pandas as pd
import math
import csv

df = pd.read_csv("/home/suman/Desktop/Doctor-recommendation-system/datasets/Training.csv")
stop_words = [
    "i",
    "me",
    "my",
    "myself",
    "we",
    "our",
    "ours",
    "ourselves",
    "you",
    "you're",
    "you've",
    "you'll",
    "you'd",
    "your",
    "yours",
    "yourself",
    "yourselves",
    "he",
    "him",
    "his",
    "himself",
    "she",
    "she's",
    "her",
    "hers",
    "herself",
    "it",
    "it's",
    "its",
    "itself",
    "they",
    "them",
    "their",
    "theirs",
    "themselves",
    "what",
    "which",
    "who",
    "whom",
    "this",
    "that",
    "that'll",
    "these",
    "those",
    "am",
    "is",
    "are",
    "was",
    "were",
    "be",
    "been",
    "being",
    "have",
    "has",
    "had",
    "having",
    "do",
    "does",
    "did",
    "doing",
    "a",
    "an",
    "the",
    "and",
    "but",
    "if",
    "or",
    "because",
    "as",
    "until",
    "while",
    "of",
    "at",
    "by",
    "for",
    "with",
    "about",
    "against",
    "between",
    "into",
    "through",
    "during",
    "before",
    "after",
    "above",
    "below",
    "to",
    "from",
    "up",
    "down",
    "in",
    "out",
    "on",
    "off",
    "over",
    "under",
    "again",
    "further",
    "then",
    "once",
    "here",
    "there",
    "when",
    "where",
    "why",
    "how",
    "all",
    "any",
    "both",
    "each",
    "few",
    "more",
    "most",
    "other",
    "some",
    "such",
    "no",
    "nor",
    "not",
    "only",
    "own",
    "same",
    "so",
    "than",
    "too",
    "very",
    "s",
    "t",
    "can",
    "will",
    "just",
    "don",
    "don't",
    "should",
    "should've",
    "now",
    "d",
    "ll",
    "m",
    "o",
    "re",
    "ve",
    "y",
    "ain",
    "aren",
    "aren't",
    "couldn",
    "couldn't",
    "didn",
    "didn't",
    "doesn",
    "doesn't",
    "hadn",
    "hadn't",
    "hasn",
    "hasn't",
    "haven",
    "haven't",
    "isn",
    "isn't",
    "ma",
    "mightn",
    "mightn't",
    "mustn",
    "mustn't",
    "needn",
    "needn't",
    "shan",
    "shan't",
    "shouldn",
    "shouldn't",
    "wasn",
    "wasn't",
    "weren",
    "weren't",
    "won",
    "won't",
    "wouldn",
    "wouldn't",
    "also",
]
columns = df.columns[:-2]


def remove_stop_words(sentence):
    new_word_list = []
    # split if the , or space is found in the sentence
    splitted_words = re.split(r"[,\s]+", sentence.lower())
    for word in splitted_words:
        if word not in stop_words:
            cleaned_word = clean_numbers_and_special_characters(word)
            new_word_list.append(cleaned_word)
    return [i for i in new_word_list if i]


def clean_numbers_and_special_characters(word):
    pattern = "[^a-zA-Z]"
    # replacing the characters which matches the pattern
    formatted_word = re.sub(pattern, "", word)
    return formatted_word


def create_vector_from_input(formatted_word_list):
    input_vector = []
    for column in columns:
        splitted_column = re.split("_", column)
        # print(splitted_column)
        input_vector.append(
            1 if set(splitted_column).issubset(set(formatted_word_list)) else 0
        )
    return input_vector


def dot_product(vector1, vector2):
    return sum([vector1[i] * vector2[i] for i in range(len(vector1))])


def magnitude(vector):
    return math.sqrt(sum([x**2 for x in vector]))


def cosine_similarity(vector1, vector2):
    return dot_product(vector1, vector2) / (magnitude(vector1) * magnitude(vector2))


def get_cosine_similarities(vec2):
    similarities = []
    with open("/home/suman/Desktop/Doctor-recommendation-system/datasets/updated_training_data.csv") as file_obj:
        reader_obj = csv.reader(file_obj)
        next(reader_obj)
        for row in reader_obj:
            int_row = [int(num) for num in row[1:]]
            # print
            result = cosine_similarity(int_row, vec2)
            similarities.append([int(row[0]), result])

    return similarities


def sort_similarities(similarities, top_n):
    sorted_scores = sorted(similarities, key=lambda x: x[1], reverse=True)
    return sorted_scores[:top_n]



if __name__ == '__main__':
    input_text = input("Enter your symptoms: ")
    formatted_list = remove_stop_words(input_text)
    vec2 = create_vector_from_input(formatted_list)
    similarities = get_cosine_similarities(vec2)
    results = sort_similarities(similarities, 5)
    for res in results:
        print(df.iloc[res[0]]["prognosis"])
    # print(result)