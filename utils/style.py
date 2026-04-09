import streamlit as st

def apply_dark_theme():
    st.markdown("""
    <style>

    header, footer {display: none !important;}
    [data-testid="stToolbar"] {display: none !important;}

    .block-container {
        padding-top: 0rem !important;
        margin-top: 0rem !important;
    }

    .stApp {
        background: linear-gradient(135deg, #0a0f1c, #1b2735, #2c5364);
        color: white !important;
    }

    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #141e30, #243b55);
    }

    section[data-testid="stSidebar"] * {
        color: white !important;
    }

    html, body, p, div, span, label {
        color: white !important;
    }

    h1, h2, h3 {
        color: #00e5ff !important;
    }

    textarea, input {
        background-color: #1e1e1e !important;
        color: white !important;
        border: 1px solid #00e5ff !important;
        border-radius: 10px !important;
    }

    .stButton > button {
        background: linear-gradient(135deg, #00e5ff, #2979ff) !important;
        color: white !important;
        border-radius: 10px;
        padding: 10px 25px;
        border: none;
    }
    /* 🔽 FIX SELECTBOX */
    div[data-baseweb="select"] > div {
        background-color: #1e1e1e !important;
        color: white !important;
        border-radius: 10px !important;
        border: 1px solid #00e5ff !important;
    }

    /* Selected text */
    div[data-baseweb="select"] span {
        color: white !important;
    }

    /* Dropdown menu */
    ul[role="listbox"] {
        background-color: #1e1e1e !important;
        color: white !important;
    }

    /* Dropdown items */
    li[role="option"] {
        color: white !important;
    }

    /* Hover effect */
    li[role="option"]:hover {
        background-color: #2979ff !important;
    }
    /* 🔥 FIX DROPDOWN OPTIONS TEXT */
    ul[role="listbox"] li {
        background-color: #1e1e1e !important;
        color: white !important;
    }

    /* When hovering */
    ul[role="listbox"] li:hover {
        background-color: #2979ff !important;
        color: white !important;
    }

    /* Selected option */
    ul[role="listbox"] li[aria-selected="true"] {
        background-color: #00e5ff !important;
        color: black !important;
    }
    /* 🔥 FORCE FIX STREAMLIT SELECTBOX DROPDOWN */

    /* Main select box */
    div[data-baseweb="select"] > div {
        background-color: #1e1e1e !important;
        color: white !important;
        border: 1px solid #00e5ff !important;
    }

    /* Selected text */
    div[data-baseweb="select"] span {
        color: white !important;
    }

    /* Dropdown container (VERY IMPORTANT) */
    div[data-baseweb="popover"] {
        background-color: #1e1e1e !important;
    }

    /* Options list */
    ul {
        background-color: #1e1e1e !important;
    }

    /* Each option text */
    li {
        background-color: #1e1e1e !important;
        color: white !important;
    }

    /* Hover */
    li:hover {
        background-color: #2979ff !important;
        color: white !important;
    }

    /* Selected option */
    li[aria-selected="true"] {
        background-color: #00e5ff !important;
        color: black !important;
    }
    </style>
    """, unsafe_allow_html=True)