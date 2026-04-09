import streamlit as st
import plotly.express as px
from utils.style import apply_dark_theme

apply_dark_theme()

st.title("📊 Dashboard")

# ===== CHECK =====
if "results_df" not in st.session_state:
    st.warning("⚠️ Please run Batch Analysis first")
    st.stop()

df = st.session_state["results_df"]

# ===== EXTRA SAFETY =====
if df.empty:
    st.warning("No data available")
    st.stop()

if "Prediction" not in df.columns:
    st.error("❌ Prediction column missing")
    st.stop()

# ===== CALCULATIONS =====
total = len(df)
genuine = (df["Prediction"] == "Legitimate").sum()
fake = (df["Prediction"] == "Fraudulent").sum()

# ===== CHART =====
st.subheader("Fake vs Genuine Reviews")

fig = px.pie(
    names=["Genuine", "Fake"],
    values=[genuine, fake],
    title="Review Distribution"
)

st.plotly_chart(fig, use_container_width=True)

# ===== INSIGHTS =====
st.markdown("### 📌 Insights")
st.write("Total Reviews:", total)
st.write("Genuine Reviews:", genuine)
st.write("Fake Reviews:", fake)

fake_percent = (fake / total) * 100 if total > 0 else 0
st.write(f"Fake Review Percentage: {round(fake_percent, 2)}%")