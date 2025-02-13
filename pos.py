from nltk.tokenize import word_tokenize

import nltk
nltk.download('averaged_perceptron_tagger_eng')

def posTagging(corpus) -> list:
    words = word_tokenize(corpus)
    processed_text = nltk.pos_tag(words)

    return processed_text
