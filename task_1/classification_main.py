from keywords import check_list
import joblib
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from textblob import TextBlob
from collections import Counter, OrderedDict

lemmatizer = WordNetLemmatizer()
cl_NB = joblib.load("cl_NB.pkl")


def get_part_of_speech(word):
    probable_part_of_speech = wordnet.synsets(word)

    pos_counts = Counter()

    pos_counts["n"] = len([item for item in probable_part_of_speech if item.pos() == "n"])
    pos_counts["v"] = len([item for item in probable_part_of_speech if item.pos() == "v"])
    pos_counts["a"] = len([item for item in probable_part_of_speech if item.pos() == "a"])
    pos_counts["r"] = len([item for item in probable_part_of_speech if item.pos() == "r"])

    most_likely_part_of_speech = pos_counts.most_common(1)[0][0]
    return most_likely_part_of_speech


def lemmatize_words_and_sentence(word):
    tokenized_words = word_tokenize(word)
    return " ".join([lemmatizer.lemmatize(token, get_part_of_speech(token)) for token in tokenized_words])


def pre_processing(input_text):
    input_text = input_text.lower()
    input_text = " ".join([lemmatize_words_and_sentence(token) for token in word_tokenize(input_text)])
    return input_text


def find_prob_sorted(input_text):
    input_text = lemmatize_words_and_sentence(input_text)
    prob_dist = cl_NB.prob_classify(input_text)
    dict_prob = dict()
    for class_ in cl_NB.labels():
        dict_prob[class_] = prob_dist.prob(str(class_))
    d_sorted_by_value = OrderedDict(sorted(dict_prob.items(), key=lambda x: x[1], reverse=True))
    return dict(d_sorted_by_value)


def is_casual(input_sentence):
    input_sentence = lemmatize_words_and_sentence(input_sentence)
    for word in check_list:
        if word in input_sentence:
            return False
    return True


def is_serach_overlapping(input_text):
    input_text = pre_processing(input_text)
    input_text = word_tokenize(input_text)
    dummy = list()
    for word in input_text:
        if word in check_list:
            dummy.append(word)
    if len(dummy) > 1:
        return True
    return False


def classify_the_text(text):
    text = pre_processing(text)

    blob = TextBlob(text, classifier=cl_NB)
    label_list = []

    for sentence in blob.sentences:
        if not is_casual(str(sentence)):
            if is_serach_overlapping(str(sentence)):
                find_prob_sorted(str(sentence))
                cat_1 = list(find_prob_sorted(str(sentence)).keys())[0]
                cat_2 = list(find_prob_sorted(str(sentence)).keys())[1]
                find_prob_sorted(str(sentence)).keys()
                print("{} : {}".format(sentence, "{}/{}".format(cat_1, cat_2)))
                label_list.append("{}/{}".format(cat_1, cat_2))

                break
            classified_sentence = sentence.classify()

            print("{} : {}".format(sentence, classified_sentence))

            label_list.append(str(classified_sentence))
        else:

            print("{} : {}".format(sentence, 'Casual'))

            label_list.append("Casual")
    print(label_list)

    if len(Counter(label_list).most_common()) > 1 and Counter(label_list).most_common()[0][0] == "Casual":
        print(Counter(label_list).most_common()[1][0])

    else:
        print(Counter(label_list).most_common()[0][0])
