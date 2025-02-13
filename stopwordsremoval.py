from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

nltk.download("stopwords")

def stopWordsRemoval(corpus) -> str:
    processed_text=""
    words = word_tokenize(corpus)

    stop_words = set(stopwords.words("english"))

    for x in words:
        if x not in stop_words:
            processed_text = processed_text + " " + x
        
    return processed_text