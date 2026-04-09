import streamlit as st
import plotly.express as px

st.title("📊 Dashboard")

# Check if analysis done
if "results_df" not in st.session_state:
    st.warning("⚠️ Please run Batch Analysis first")
else:
    df = st.session_state["results_df"]

    total = len(df)
    genuine = (df["Prediction"] == "Legitimate").sum()
    fake = (df["Prediction"] == "Fraudulent").sum()

    st.subheader("Fake vs Genuine Reviews")

    # Pie chart
    fig = px.pie(
        names=["Genuine", "Fake"],
        values=[genuine, fake],
        title="Review Distribution"
    )
    st.plotly_chart(fig, use_container_width=True)

    # Extra insights
    st.markdown("### 📌 Insights")
    st.write("Total Reviews:", total)
    st.write("Genuine Reviews:", genuine)
    st.write("Fake Reviews:", fake)

    fake_percent = (fake / total) * 100 if total > 0 else 0
    st.write(f"Fake Review Percentage: {round(fake_percent,2)}%")