import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from textblob import TextBlob

# Load dataset
df = pd.read_csv("/home/aman/Desktop/Project/Customer Support ChatBot/Mental_Health_FAQ.csv")

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess(text):
    text = str(text).lower()
    text = re.sub(r'[^\w\s]', '', text)

    tokens = word_tokenize(text)

    tokens = [
        lemmatizer.lemmatize(word)
        for word in tokens
        if word not in stop_words
    ]

    return " ".join(tokens)

def correct_spelling(text):
    return str(TextBlob(text).correct())

df["processed_question"] = df["Questions"].apply(preprocess)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["processed_question"])

def chatbot(user_query):
    user_query = correct_spelling(user_query)
    query_processed = preprocess(user_query)

    query_vector = vectorizer.transform([query_processed])

    similarities = cosine_similarity(query_vector, X)

    best_match = similarities.argmax()
    score = similarities[0][best_match]

    if score < 0.3:
        return "Sorry, I don't understand that question."

    return df.iloc[best_match]["Answers"]
