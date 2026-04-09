import streamlit as st

# ✅ PAGE CONFIG (ONLY ONCE)
st.set_page_config(page_title="Fake Review Detection", layout="wide")

# ================= 🎨 FULL UI CSS =================
st.markdown("""
<style>

/* 🚨 REMOVE TOP WHITE BAR COMPLETELY */
header {display: none !important;}
footer {display: none !important;}
[data-testid="stToolbar"] {display: none !important;}
[data-testid="stDecoration"] {display: none !important;}
[data-testid="stStatusWidget"] {display: none !important;}

/* 🚨 REMOVE TOP SPACE */
.block-container {
    padding-top: 0rem !important;
    margin-top: 0rem !important;
}

section.main > div {
    padding-top: 0rem !important;
}

/* 🌌 DARK BACKGROUND */
.stApp {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    color: white;
}

/* 🔵 SIDEBAR */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #141e30, #243b55);
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

/* 📺 FULL WIDTH */
.block-container {
    max-width: 100% !important;
    padding-left: 3rem;
    padding-right: 3rem;
}

/* 🧠 TITLE */
.big-title {
    font-size: 46px;
    font-weight: bold;
    text-align: center;
    color: #00e5ff;
    text-shadow: 2px 2px 15px rgba(0,0,0,0.6);
}

/* 📦 CONTENT BOX */
.section-box {
    font-size: 20px;
    padding: 30px;
    border-radius: 15px;
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(10px);
    box-shadow: 0 0 20px rgba(0,0,0,0.5);
}

/* 🔘 BUTTON */
.stButton>button {
    background: linear-gradient(135deg, #00e5ff, #2979ff);
    color: white !important;
    border-radius: 10px;
    padding: 10px 25px;
    font-size: 16px;
    border: none;
}

.stButton>button:hover {
    transform: scale(1.05);
}

/* 📝 INPUT */
textarea {
    border-radius: 10px !important;
    border: 2px solid #00e5ff !important;
    background-color: #1e1e1e !important;
    color: white !important;
}

</style>
""", unsafe_allow_html=True)

# ================= 🚀 SIDEBAR =================
st.sidebar.markdown("## 🚀 Navigation")
st.sidebar.markdown("Select a module")

# ================= 🏠 MAIN PAGE =================
st.markdown("<br>", unsafe_allow_html=True)

st.title("AI-Based Fake Review Detection and Sentiment Analysis System")

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class="section-box">

<h2>Welcome to the System</h2>

<ul>
<li>🔍 Detect Fake Reviews</li>
<li>😊 Perform Sentiment Analysis</li>
<li>🌍 Perform Multilingual Review Analysis</li>
<li>📊 Analyze Multiple Reviews</li>
<li>📄 Show Dashboard and Reports</li>
</ul>

Use the sidebar to navigate to different modules.

</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("---")