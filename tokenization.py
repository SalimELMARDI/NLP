import nltk
nltk.download('punkt_tab')

from nltk.tokenize import sent_tokenize, word_tokenize

def sentenceTokenization(corpus) -> str:
    processed_text = sent_tokenize(corpus)
    return processed_text

def wordTokenization(corpus) -> str:
    processed_text = word_tokenize(corpus)
    return processed_text