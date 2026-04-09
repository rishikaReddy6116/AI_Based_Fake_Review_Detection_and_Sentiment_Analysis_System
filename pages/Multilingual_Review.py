import streamlit as st
from deep_translator import GoogleTranslator
from utils.model_utils import text_classification
from utils.style import apply_dark_theme

apply_dark_theme()

st.title("🌍 Multilingual Review Analysis")

# 🌐 Language selection
languages = {
    "English": "en",
    "Telugu": "te",
    "Hindi": "hi",
    "Tamil": "ta",
    "Kannada": "kn"
}

selected_lang = st.selectbox("Select Language", list(languages.keys()))

# 📝 Input
review = st.text_area("Enter Review")

# 🔘 Button
if st.button("Analyze"):

    if review.strip() == "":
        st.warning("Please enter a review")
    else:
        # 🔄 Translate to English
        translated = GoogleTranslator(source='auto', target='en').translate(review)

        st.write("🔄 Translated Review:", translated)

        # 🤖 Prediction
        result, confidence, fraud_score, explanation = text_classification(translated)

        # 🎯 Output
        if result == "Legitimate":
            st.success(f"✅ Legitimate ({round(confidence,2)}%)")
        elif result == "Fraudulent":
            st.error(f"❌ Fraudulent ({round(confidence,2)}%)")
        else:
            st.warning(f"⚠️ Mixed ({round(confidence,2)}%)")

        st.write("📊 Fraud Score:", fraud_score)
        st.write("💡 Explanation:", explanation)