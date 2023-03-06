import joblib as jb
from .text_processing import create_vector_from_input, remove_stop_words

model = jb.load('/home/suman/Desktop/Doctor-recommendation-system/HospitalManagement/trained_model')
def predict_disease(input_vec):

    predicted = model.predict(input_vec)
    print(predicted)
    predict_prob = model.predict_proba(input_vec)
    return predict_prob


def give_disease_with_naive_bayes(input_text):
    disease_result = []
    formatted_list = remove_stop_words(input_text)
    print(formatted_list)
    vec2 = create_vector_from_input(formatted_list)
    if all(val == 0 for val in vec2):
        return None
    # print(vec2)
    similarities = predict_disease(vec2)
    # results = sort_similarities(similarities)
    # for res in results:
    #     if res[1] > 0.2:
    #         disease_result.append(df.iloc[res[0]]["prognosis"])
    # return list(set(disease_result))
    return similarities

if __name__ == '__main__':
    input_text = input("Enter your text")
    formatted_list = remove_stop_words(input_text)
    vec1 = create_vector_from_input(formatted_list)
    print(predict_disease(vec1))


