import nltk
from nltk.tokenize import word_tokenize

nltk.download('maxent_ne_chunker_tab')
nltk.download('words')

def namedEntityRecognition(corpus) -> list:
    words = word_tokenize(corpus)
    return (nltk.ne_chunk(nltk.pos_tag(words)))