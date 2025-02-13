from nltk.stem import PorterStemmer,  RegexpStemmer, SnowballStemmer
from nltk.tokenize import word_tokenize

def porterStemming(corpus) -> str:
    processed_text=""
    words = word_tokenize(corpus)
    ps = PorterStemmer()
    for x in words:
        processed_text= processed_text + " " + (ps.stem(x))
    return processed_text


def regexpStemmer(corpus) -> str:
    processed_text=""
    words = word_tokenize(corpus)
    rs = RegexpStemmer('ing$|able$|s$')
    for x in words:
        processed_text= processed_text + " " + (rs.stem(x))
    return processed_text


def snowballStemmer(corpus) -> str:
    processed_text=""
    words = word_tokenize(corpus)
    ss = SnowballStemmer("english")
    for x in words:
        processed_text= processed_text + " " + (ss.stem(x))
    return processed_text