from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

UNCERTAINTY_WORDS = ["i don't know", "not sure", "cannot", "uncertain"]

def response_length(text):
    return len(text.split())

def uncertainty_flag(text):
    return any(word in text.lower() for word in UNCERTAINTY_WORDS)

def similarity_score(a, b):
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform([a, b])
    return cosine_similarity(tfidf)[0][1]
