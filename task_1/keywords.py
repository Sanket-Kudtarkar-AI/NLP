from textblob.classifiers import NaiveBayesClassifier
import joblib
from nltk.stem import WordNetLemmatizer

from nltk.tokenize import word_tokenize

from collections import Counter
from nltk.corpus import wordnet

keywords = [

    ('expensive', 'Pricing and Budget'),
    ('budget', 'Pricing and Budget'),
    ('cheaper', 'Pricing and Budget'),
    ('affordable', 'Pricing and Budget'),
    ('price', 'Pricing and Budget'),
    ('offer', 'Pricing and Budget'),
    ('concession', 'Pricing and Budget'),
    ('free', 'Pricing and Budget'),
    ('downsized', 'Pricing and Budget'),
    ('bought', 'Pricing and Budget'),
    ('locked', 'Pricing and Budget'),
    ('contract', 'Pricing and Budget'),

    ('vendor', 'Competition Comparisions'),
    ('product', 'Competition Comparisions'),
    ('comparison', 'Competition Comparisions'),
    ('option', 'Competition Comparisions'),
    ('suggestion', 'Competition Comparisions'),
    ('automatically', 'Competition Comparisions'),
    ('automatic', 'Competition Comparisions'),
    ('similar space', 'Competition Comparisions'),
    ('like us', 'Competition Comparisions'),
    ('close to us', 'Competition Comparisions'),
    ('plan', 'Competition Comparisions'),
    ('support', 'Competition Comparisions'),
    ('competition', 'Competition Comparisions'),
    ('version', 'Competition Comparisions'),

    ('extra', 'Product Features'),
    ('feature', 'Product Features'),
    ('summary', 'Product Features'),
    ('automatic', 'Product Features'),
    ('automatically', 'Product Features'),

    ('privacy', 'Pocilies and Terms'),
    ('policy', 'Pocilies and Terms'),
    ('gdpr', 'Pocilies and Terms'),
    ('legal', 'Pocilies and Terms'),
    ('safe', 'Pocilies and Terms'),
    ('security', 'Pocilies and Terms'),

    ('industry', 'Customer Qualification'),
    ('size', 'Customer Qualification'),
    ('location', 'Customer Qualification'),
    ('employee', 'Customer Qualification'),
    ('market', 'Customer Qualification'),
    ('region', 'Customer Qualification'),
    ('language', 'Customer Qualification'),
    ('team', 'Customer Qualification'),
    ('remote', 'Customer Qualification'),
    ('time zone', 'Customer Qualification'),
    ('team size', 'Customer Qualification')
]
check_list = list()
train = list()
lemmatizer = WordNetLemmatizer()


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


def add_to_training(word, category):
    word = word.lower()
    word = lemmatize_words_and_sentence(word)
    train.append((word, str(category)))
    check_list.append(word)


for keyword in keywords:
    add_to_training(keyword[0], keyword[1])

cl_NB = NaiveBayesClassifier(train)

joblib.dump(cl_NB, 'cl_NB.pkl')
