from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

import nltk
nltk.download('wordnet')

def wordnetLemmatizer(corpus):
    processed_text=""
    words = word_tokenize(corpus)
    lemmatizer = WordNetLemmatizer()
    for x in words:
        processed_text = processed_text + " " + (lemmatizer.lemmatize(x))
    return processed_text
