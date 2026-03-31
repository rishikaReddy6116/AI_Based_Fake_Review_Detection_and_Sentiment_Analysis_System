# ================= LIBRARIES =================
import streamlit as st
import pickle
import nltk
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import re
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from scipy.sparse import hstack

# ================= LOAD MODEL FILES =================
model = pickle.load(open('data and pickle files/best_model.pkl','rb')) 
tfidf = pickle.load(open('data and pickle files/tfidf.pkl','rb'))
feature_columns = pickle.load(open('data and pickle files/feature_columns.pkl','rb'))

nltk.download('stopwords')

# ================= TEXT PREPROCESSING =================
sw = set(stopwords.words('english'))
stemmer = PorterStemmer()

def text_preprocessing(text):
    txt = TextBlob(text)
    result = txt.correct()

    removed_special_characters = re.sub("[^a-zA-Z]", " ", str(result))
    tokens = removed_special_characters.lower().split()

    cleaned = []
    for token in tokens:
        if token not in sw:
            cleaned.append(stemmer.stem(token))

    return " ".join(cleaned)

# ================= EXTRA FEATURES =================
def extract_features(text):
    text = str(text)
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

# ================= FAKE REVIEW DETECTION =================
def text_classification(text):
    cleaned_review = text_preprocessing(text)

    # ML prediction
    text_vector = tfidf.transform([cleaned_review])
    feature_vector = extract_features(text).values
    final_input = hstack([text_vector, feature_vector])

    ml_prediction = model.predict(final_input)[0]
    probability = model.predict_proba(final_input)
    confidence = max(probability[0]) * 100

    # Rule-based fake detection (VERY IMPORTANT)
    words = text.lower().split()
    repeated_words = len(words) - len(set(words))
    exclamations = text.count('!')
    capitals = sum(1 for c in text if c.isupper())

    if repeated_words >= 2 or exclamations >= 2 or capitals >= 5:
        final_prediction = "Fraudulent"
    else:
        final_prediction = "Legitimate"

    # Display result
    if final_prediction == "Legitimate":
        st.success(f" Legitimate Review (Confidence: {round(confidence,2)}%)")
    else:
        st.error(f" Fraudulent Review (Confidence: {round(confidence,2)}%)")

    return final_prediction
# ================= SENTIMENT ANALYSIS =================
def analyze_sentiment(review):
    clean_review = text_preprocessing(review)
    blob = TextBlob(clean_review)

    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    return clean_review, polarity, subjectivity

# ================= DASHBOARD =================
def show_dashboard(polarity, subjectivity):

    st.markdown("## Sentiment Dashboard")

    fig_gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=polarity,
        title={'text': "Sentiment Polarity"},
        gauge={'axis': {'range': [-1, 1]}}
    ))
    st.plotly_chart(fig_gauge)

    df = pd.DataFrame({
        "Metric": ["Polarity", "Subjectivity"],
        "Value": [abs(polarity), subjectivity]
    })

    fig_bar = px.bar(df, x="Metric", y="Value", range_y=[0,1],
                     title="Polarity vs Subjectivity")
    st.plotly_chart(fig_bar)

# ================= BATCH ANALYZER =================
def batch_analyze_reviews(reviews_list):

    results = []
    polarities = []

    for review in reviews_list:
        if review.strip() != "":
            cleaned_review = text_preprocessing(review)

            text_vector = tfidf.transform([cleaned_review])
            feature_vector = extract_features(review).values

            final_input = hstack([text_vector, feature_vector])

            # ML prediction
            prediction = model.predict(final_input)
            prob = model.predict_proba(final_input)
            confidence = max(prob[0]) * 100

            # RULE-BASED DETECTION (IMPORTANT)
            words = review.lower().split()
            repeated_words = len(words) - len(set(words))
            exclamations = review.count('!')
            capitals = sum(1 for c in review if c.isupper())

            if repeated_words >= 2 or exclamations >= 2 or capitals >= 5:
                final_prediction = "Fraudulent"
            else:
                final_prediction = "Legitimate"

            # Sentiment
            blob = TextBlob(cleaned_review)
            polarity = blob.sentiment.polarity

            results.append({
                "Review": review,
                "Prediction": final_prediction,
                "Confidence (%)": round(confidence, 2),
                "Polarity": round(polarity, 3)
            })

            polarities.append(polarity)

    df = pd.DataFrame(results)

    return df, polarities
# ================= STREAMLIT APP =================
def main():

    st.title("AI Based Fake Review Detection and Sentiment Analysis System")

    st.markdown("---")

    # ========== SINGLE REVIEW ==========
    st.header("🔎 Single Review Analysis")

    review = st.text_area("Enter Review Below:")

    if st.button("Analyze Review"):

        if review.strip() == "":
            st.warning("Please enter a review.")
        else:

            st.subheader("Fake Review Detection")
            result = text_classification(review)

            st.markdown("---")

            st.subheader("Sentiment Analysis")

            clean_review, polarity, subjectivity = analyze_sentiment(review)

            st.write("Cleaned Review:", clean_review)
            st.write("Polarity Score:", round(polarity, 3))
            st.write("Subjectivity Score:", round(subjectivity, 3))

            st.markdown("---")
            show_dashboard(polarity, subjectivity)

    # ========== BATCH ANALYSIS ==========
    st.markdown("---")
    st.header("Multi-Review Batch Analyzer")

    batch_input = st.text_area(
        "Paste multiple reviews (One review per line):",
        height=200
    )

    if st.button("Analyze Batch Reviews"):

        reviews_list = batch_input.split("\n")

        df_results, polarities = batch_analyze_reviews(reviews_list)

        if len(df_results) == 0:
            st.warning("Please enter valid reviews.")
        else:
            st.subheader("Batch Analysis Results")
            st.dataframe(df_results)

            total = len(df_results)
            legit_count = (df_results["Prediction"] == "Legitimate").sum()
            fraud_count = (df_results["Prediction"] == "Fraudulent").sum()

            avg_polarity = sum(polarities) / len(polarities)

            st.subheader("Summary Statistics")
            st.write("Total Reviews:", total)
            st.write("Legitimate Reviews:", legit_count)
            st.write("Fraudulent Reviews:", fraud_count)
            st.write("Average Polarity:", round(avg_polarity, 3))

            fig = px.pie(
                names=["Legitimate", "Fraudulent"],
                values=[legit_count, fraud_count],
                title="Review Classification Distribution"
            )
            st.plotly_chart(fig)

            fig2 = px.histogram(
                df_results,
                x="Polarity",
                nbins=10,
                title="Polarity Distribution"
            )
            st.plotly_chart(fig2)

# ================= RUN APP =================
if __name__ == "__main__":
    main()