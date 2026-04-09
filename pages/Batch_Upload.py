import streamlit as st
import pandas as pd
from utils import text_classification

st.title("📊 Batch Review Analysis")

batch_input = st.text_area("Enter multiple reviews (one per line)")

if st.button("Analyze Batch"):

    reviews = batch_input.split("\n")
    results = []

    for review in reviews:
        if review.strip() != "":

            # 🔍 Only classification (NO sentiment)
            pred, conf, fraud_score, explanation = text_classification(review)

            results.append({
                "Review": review,
                "Prediction": pred,
                "Confidence": round(conf, 2),
                "Fraud Score": fraud_score,
                "Explanation": explanation
            })

    df = pd.DataFrame(results)

    # ===== DISPLAY =====
    st.subheader("📋 Results")

    def highlight(row):
        if row["Prediction"] == "Fraudulent":
            return ['background-color: #f8d7da'] * len(row)
        elif row["Prediction"] == "Mixed":
            return ['background-color: #fff3cd'] * len(row)
        else:
            return ['background-color: #d4edda'] * len(row)

    st.dataframe(df.style.apply(highlight, axis=1))

    # Save for dashboard
    st.session_state["results_df"] = df