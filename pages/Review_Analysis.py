import streamlit as st
from utils import text_classification, analyze_sentiment
from googletrans import Translator

translator = Translator()

# ===== UI HEADINGS =====
st.markdown('<p class="big-title">AI Based Fake Review Detection and Sentiment Analysis System</p>', unsafe_allow_html=True)
st.markdown("---")
st.markdown('<p class="section-title">🔎 Single Review Analysis</p>', unsafe_allow_html=True)

# ===== INPUT =====
review = st.text_area("Enter Review")

# ===== BUTTON =====
if st.button("Analyze"):

    # 🌍 Language Detection
    lang = translator.detect(review).lang
    st.write("🌐 Detected Language:", lang)

    # ===== MODEL OUTPUT =====
    result, confidence, fraud_score, explanation = text_classification(review)

    # ===== RESULT DISPLAY (3 CASES) =====
    if result == "Legitimate":
        st.markdown(
            f'<div class="result-box-legit">✅ Legitimate Review (Confidence: {round(confidence,2)}%)</div>',
            unsafe_allow_html=True
        )

    elif result == "Fraudulent":
        st.markdown(
            f'<div class="result-box-fraud">❌ Fraudulent Review (Confidence: {round(confidence,2)}%)</div>',
            unsafe_allow_html=True
        )

    else:
        st.markdown(
            f'<div style="background-color:#fff3cd;padding:15px;border-radius:10px;color:#856404;font-size:18px;">⚠️ Mixed / Neutral Review (Confidence: {round(confidence,2)}%)</div>',
            unsafe_allow_html=True
        )

    # ===== EXTRA INFO =====
    st.write("📊 Fraud Score:", fraud_score)
    st.write("💡 Explanation:", explanation)

    # ===== FRAUD SCORE PROGRESS BAR =====
    st.progress(min(fraud_score / 100, 1.0))

    # ===== SENTIMENT =====
    clean, polarity, subjectivity = analyze_sentiment(review)

    st.markdown("### 😊 Sentiment Analysis")
    st.write("Polarity:", round(polarity, 3))
    st.write("Subjectivity:", round(subjectivity, 3))