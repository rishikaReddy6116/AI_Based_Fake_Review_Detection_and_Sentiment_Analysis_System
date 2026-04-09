import streamlit as st
import plotly.express as px

st.title("📄 Dynamic Report")

# Check if data exists
if "results_df" not in st.session_state:
    st.warning("⚠️ Please run Batch Analysis first")
else:
    df = st.session_state["results_df"]

    total = len(df)
    fake = (df["Prediction"] == "Fraudulent").sum()
    genuine = (df["Prediction"] == "Legitimate").sum()

    positive = (df["Polarity"] > 0).sum()
    negative = (df["Polarity"] < 0).sum()

    # ===== Summary =====
    st.subheader("📊 Summary")
    st.write("Total Reviews:", total)
    st.write("Fake Reviews:", fake)
    st.write("Genuine Reviews:", genuine)
    st.write("Positive Reviews:", positive)
    st.write("Negative Reviews:", negative)

    # ===== Pie Chart =====
    fig = px.pie(
        names=["Genuine", "Fraudulent"],
        values=[genuine, fake],
        title="Fake vs Genuine Distribution"
    )
    st.plotly_chart(fig)

    # ===== Sentiment Chart =====
    fig2 = px.bar(
        x=["Positive", "Negative"],
        y=[positive, negative],
        title="Sentiment Analysis"
    )
    st.plotly_chart(fig2)

    # ===== Download Report =====
    csv = df.to_csv(index=False)

    st.download_button(
        "📥 Download Report",
        csv,
        file_name="analysis_report.csv",
        mime="text/csv"
    )