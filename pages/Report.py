import streamlit as st
import plotly.express as px
from utils.style import apply_dark_theme

apply_dark_theme()

st.title("📄 Dynamic Report")

# ===== CHECK =====
if "results_df" not in st.session_state:
    st.warning("⚠️ Please run Batch Analysis first")
    st.stop()

df = st.session_state["results_df"]

# ===== SAFETY =====
if df.empty:
    st.warning("No data available")
    st.stop()

if "Prediction" not in df.columns:
    st.error("❌ Prediction column missing")
    st.stop()

# ===== CALCULATIONS =====
total = len(df)
fake = (df["Prediction"] == "Fraudulent").sum()
genuine = (df["Prediction"] == "Legitimate").sum()

# (Only if Polarity exists)
if "Polarity" in df.columns:
    positive = (df["Polarity"] > 0).sum()
    negative = (df["Polarity"] < 0).sum()
else:
    positive = negative = 0

# ===== SUMMARY =====
st.subheader("📊 Summary")
st.write("Total Reviews:", total)
st.write("Fake Reviews:", fake)
st.write("Genuine Reviews:", genuine)
st.write("Positive Reviews:", positive)
st.write("Negative Reviews:", negative)

# ===== PIE CHART =====
fig = px.pie(
    names=["Genuine", "Fraudulent"],
    values=[genuine, fake],
    title="Fake vs Genuine Distribution"
)
st.plotly_chart(fig, use_container_width=True)

# ===== SENTIMENT CHART =====
fig2 = px.bar(
    x=["Positive", "Negative"],
    y=[positive, negative],
    title="Sentiment Analysis"
)
st.plotly_chart(fig2, use_container_width=True)

# ===== DOWNLOAD =====
csv = df.to_csv(index=False)

st.download_button(
    "📥 Download Report",
    csv,
    file_name="analysis_report.csv",
    mime="text/csv"
)