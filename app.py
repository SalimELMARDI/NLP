import streamlit as st
from tokenization import sentenceTokenization, wordTokenization
from stemming import porterStemming, regexpStemmer, snowballStemmer
from stopwordsremoval import stopWordsRemoval
from lemmatization import wordnetLemmatizer
from ner import namedEntityRecognition
from pos import posTagging

# Set page configuration
st.set_page_config(
    page_title="NLP Tool by CODE",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for dark blue theme and styling
st.markdown(
    """
    <style>
    /* Global Styles */
    body, .reportview-container {
        background-color: #182C46; /* Dark blue background */
        color: white; /* White text */
        font-family: Arial, sans-serif;
    }

    /* Sidebar Styles */
    .sidebar .sidebar-content {
        background-color: #182C46; /* Dark blue background */
        color: white; /* White text */
    }
    .sidebar .sidebar-content .stMarkdown {
        color: white; /* Ensure sidebar text is white */
    }

    /* Button Styles */
    .stButton button {
        background-color: #0056b3; /* Button primary color */
        color: white; /* Button text color */
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stButton button:hover {
        background-color: #003d80; /* Button hover color */
    }

    /* Input Field Styles */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        color: white; /* Input field text color */
        background-color: #2c3e50; /* Input field background */
        border: 1px solid #34495e;
        border-radius: 5px;
    }

    /* Dropdown Styles */
    .stSelectbox>div>div>select {
        color: white; /* Dropdown text color */
        background-color: #2c3e50; /* Dropdown background */
        border: 1px solid #34495e;
        border-radius: 5px;
    }

    /* Footer Styles */
    footer {visibility: hidden;} /* Hide default footer */

    /* Custom Footer */
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #182C46; /* Dark blue background */
        color: white; /* White text */
        text-align: center;
        padding: 10px;
        font-size: 14px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header Section
st.title("NLP Tool by CODE 📚")
st.write("Visualize various NLP preprocessing tasks interactively!")

# Logo Placeholder
st.sidebar.image("logo.jpg", width=200)  # Replace "logo.png" with your actual logo file path

# Text Input
corpus = st.text_area("Enter your text here!", height=150)
st.write(f"You wrote {len(corpus)} characters.")

techniques = "NA"
subTechniques = "NA"

def addTechniques() -> None:
    global techniques
    techniques = st.sidebar.selectbox("Select a Technique", (
        "Tokenization", "Stemming", "Lemmatization", "Stop words removal", 
        "Parts of Speech (POS) Tagging", "Named Entity Recognition (NER)"
    ))

def addSubTechniques(techniques) -> None:
    global subTechniques
    if techniques == "Tokenization":
        subTechniques = st.sidebar.selectbox("Select a Sub-Technique", ("Sentence Tokenization", "Word Tokenization"))
    elif techniques == "Stemming":
        subTechniques = st.sidebar.selectbox("Select a Sub-Technique", ("Porter Stemmer", "Regexp Stemmer", "Snowball Stemmer"))
    elif techniques == "Lemmatization":
        subTechniques = st.sidebar.selectbox("Select a Sub-Technique", ("Wordnet Lemmatizer",))
    elif techniques == "Stop words removal":
        subTechniques = st.sidebar.selectbox("Select a Sub-Technique", ("English",))
    elif techniques == "Parts of Speech (POS) Tagging":
        subTechniques = st.sidebar.selectbox("Select a Sub-Technique", ("using NLTK",))
    elif techniques == "Named Entity Recognition (NER)":
        subTechniques = st.sidebar.selectbox("Select a Sub-Technique", ("MaxEnt NE Chunker",))

def explanation(subTechniques) -> str:
    if subTechniques == "Sentence Tokenization":
        return "Sentence tokenization in NLP is the process of breaking down a large piece of text into individual sentences."
    elif subTechniques == "Word Tokenization":
        return "Word tokenization in NLP is the process of breaking down text into individual words or tokens."
    elif subTechniques == "Porter Stemmer":
        return "Porter Stemming is an algorithm used in NLP to reduce words to their base or root form."
    elif subTechniques == "Regexp Stemmer":
        return "Regexp Stemming is a method used in NLP to reduce words to their base or root form using regular expressions."
    elif subTechniques == "Snowball Stemmer":
        return "Snowball Stemming is a stemming algorithm used in NLP to reduce words to their base or root form with better accuracy."
    elif subTechniques == "Wordnet Lemmatizer":
        return "WordNet Lemmatization is a process in NLP that uses a lexical database called WordNet to map words to their base or dictionary form."
    elif subTechniques == "English":
        return "Stop words removal is a process in NLP that involves removing common words like 'the', 'and', 'a', etc., from a text dataset."
    elif subTechniques == "using NLTK":
        return "Parts of Speech (POS) tagging is a process in NLP that identifies the grammatical category of each word in a sentence."
    elif subTechniques == "MaxEnt NE Chunker":
        return "Named Entity Recognition (NER) is a process in NLP that identifies and categorizes named entities in unstructured text."

addTechniques()
addSubTechniques(techniques)

if st.button("Start", type="primary"):
    if techniques == "Tokenization" and subTechniques == "Sentence Tokenization":
        st.write(explanation(subTechniques))
        st.success("Result:")
        processed_text = sentenceTokenization(corpus)
        st.write(processed_text)
    elif techniques == "Tokenization" and subTechniques == "Word Tokenization":
        st.write(explanation(subTechniques))
        st.success("Result:")
        processed_text = wordTokenization(corpus)
        st.write(processed_text)
    elif techniques == "Stemming" and subTechniques == "Porter Stemmer":
        st.write(explanation(subTechniques))
        st.success("Result:")
        processed_text = porterStemming(corpus)
        st.write(processed_text)
    elif techniques == "Stemming" and subTechniques == "Regexp Stemmer":
        st.write(explanation(subTechniques))
        st.success("Result:")
        processed_text = regexpStemmer(corpus)
        st.write(processed_text)
    elif techniques == "Stemming" and subTechniques == "Snowball Stemmer":
        st.write(explanation(subTechniques))
        st.success("Result:")
        processed_text = snowballStemmer(corpus)
        st.write(processed_text)
    elif techniques == "Lemmatization" and subTechniques == "Wordnet Lemmatizer":
        st.write(explanation(subTechniques))
        st.success("Result:")
        processed_text = wordnetLemmatizer(corpus)
        st.write(processed_text)
    elif techniques == "Stop words removal" and subTechniques == "English":
        st.write(explanation(subTechniques))
        st.success("Result:")
        processed_text = stopWordsRemoval(corpus)
        st.write(processed_text)
    elif techniques == "Parts of Speech (POS) Tagging" and subTechniques == "using NLTK":
        st.write(explanation(subTechniques))
        st.success("Result:")
        processed_text = posTagging(corpus)
        st.write(processed_text)
    elif techniques == "Named Entity Recognition (NER)" and subTechniques == "MaxEnt NE Chunker":
        st.write(explanation(subTechniques))
        st.success("Result:")
        processed_text = namedEntityRecognition(corpus)
        st.write(processed_text)

# Footer
st.markdown(
    """
    <div class="footer">
        Made with ❤️ by CODE
    </div>
    """,
    unsafe_allow_html=True,
)