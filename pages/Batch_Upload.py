import streamlit as st
import pandas as pd
from utils.model_utils import text_classification
from utils.style import apply_dark_theme

apply_dark_theme()

st.title("📊 Batch Review Analysis")

batch_input = st.text_area("Enter multiple reviews")

if st.button("Analyze Batch"):

    reviews = batch_input.split("\n")
    results = []

    for review in reviews:
        if review.strip() != "":
            pred, conf, fraud_score, explanation = text_classification(review)

            results.append({
                "Review": review,
                "Prediction": pred,
                "Confidence": round(conf, 2)
            })

    df = pd.DataFrame(results)

    # ✅ THIS LINE FIXES YOUR ISSUE
    st.session_state["results_df"] = df

    st.dataframe(df)