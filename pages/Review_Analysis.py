import streamlit as st
from utils.model_utils import text_classification, analyze_sentiment
from utils.style import apply_dark_theme

apply_dark_theme()

# ===== UI HEADINGS =====
st.title("🔎 Single Review Analysis")

# ===== INPUT =====
review = st.text_area("Enter Review")

# ===== BUTTON =====
if st.button("Analyze"):

    # ===== MODEL OUTPUT =====
    result, confidence, fraud_score, explanation = text_classification(review)

    # ===== RESULT DISPLAY =====
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
            f'<div class="result-box-mixed">⚠️ Mixed Review (Confidence: {round(confidence,2)}%)</div>',
            unsafe_allow_html=True
        )

    # ===== EXTRA INFO =====
    st.write("📊 Fraud Score:", fraud_score)
    st.write("💡 Explanation:", explanation)

    # ===== PROGRESS BAR =====
    st.progress(min(fraud_score / 100, 1.0))

    # ===== SENTIMENT =====
    clean, polarity, subjectivity = analyze_sentiment(review)

    st.markdown("### 😊 Sentiment Analysis")
    st.write("Polarity:", round(polarity, 3))
    st.write("Subjectivity:", round(subjectivity, 3))