import pickle
import nltk
import re
import pandas as pd
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from scipy.sparse import hstack
from deep_translator import GoogleTranslator

# Download once
nltk.download('stopwords')

# ===== LOAD MODELS =====
model = pickle.load(open('data and pickle files/best_model.pkl','rb'))
tfidf = pickle.load(open('data and pickle files/tfidf.pkl','rb'))
feature_columns = pickle.load(open('data and pickle files/feature_columns.pkl','rb'))

sw = set(stopwords.words('english'))
stemmer = PorterStemmer()

# ================= TEXT PREPROCESSING =================
def text_preprocessing(text):
    text = re.sub("[^a-zA-Z]", " ", str(text))
    tokens = text.lower().split()
    cleaned = [stemmer.stem(word) for word in tokens if word not in sw]
    return " ".join(cleaned)

# ================= TRANSLATION =================
def translate_to_english(text):
    try:
        return GoogleTranslator(source='auto', target='en').translate(text)
    except:
        return text

# ================= EXTRA FEATURES =================
def extract_features(text):
    words = text.split()
    features = {
        'length': len(text),
        'exclamation_count': text.count('!'),
        'capital_count': sum(1 for c in text if c.isupper()),
        'word_count': len(words),
        'unique_words': len(set(words)),
        'unique_ratio': len(set(words))/len(words) if len(words)>0 else 0,
        'repeated_words': len(words)-len(set(words))
    }
    return pd.DataFrame([features])[feature_columns]

# ================= MAIN MODEL FUNCTION =================
def text_classification(text):

    # 🌐 Translate
    translated_text = translate_to_english(text)

    # Preprocess
    cleaned_review = text_preprocessing(translated_text)

    # Vectorization
    text_vector = tfidf.transform([cleaned_review])
    feature_vector = extract_features(translated_text).values
    final_input = hstack([text_vector, feature_vector])

    # ML Prediction
    ml_prediction = model.predict(final_input)[0]
    probability = model.predict_proba(final_input)
    confidence = max(probability[0]) * 100

    # RULE FEATURES
    words = translated_text.lower().split()
    repeated_words = len(words) - len(set(words))
    exclamations = translated_text.count('!')
    capitals = sum(1 for c in translated_text if c.isupper())

    spam_words = ["best", "amazing", "wow", "superb", "must", "buy", "100"]
    spam_count = sum(1 for w in words if w in spam_words)

    # SENTIMENT
    blob = TextBlob(translated_text)
    polarity = blob.sentiment.polarity

    negative_words = ["bad", "worst", "stopped", "damaged", "poor", "issue", "problem"]
    positive_words = ["good", "great", "excellent", "amazing"]

    neg_count = sum(1 for w in words if w in negative_words)
    pos_count = sum(1 for w in words if w in positive_words)

    # FRAUD SCORE
    fraud_score = 0

    if repeated_words >= 1:
        fraud_score += 25
    if exclamations >= 2:
        fraud_score += 25
    if capitals >= 3:
        fraud_score += 15
    if spam_count >= 2:
        fraud_score += 25
    if ml_prediction == 1:
        fraud_score += 10

    # ================= FINAL DECISION =================
    if polarity < 0:
        prediction = "Legitimate"
        explanation = "Negative genuine review"

    elif fraud_score >= 60:
        prediction = "Fraudulent"
        explanation = "Spam patterns detected"

    elif pos_count > 0 and neg_count > 0:
        prediction = "Mixed"
        explanation = "Contains both positive and negative opinions"

    elif polarity > 0.85 and spam_count >= 2:
        prediction = "Fraudulent"
        explanation = "Overly promotional review"

    else:
        prediction = "Legitimate"
        explanation = "Looks genuine"

    return prediction, confidence, fraud_score, explanation

# ================= SENTIMENT =================
def analyze_sentiment(review):
    clean_review = text_preprocessing(review)
    blob = TextBlob(clean_review)
    return clean_review, blob.sentiment.polarity, blob.sentiment.subjectivity