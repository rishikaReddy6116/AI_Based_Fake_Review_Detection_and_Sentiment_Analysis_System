# AI-Based Fake Review Detection and Sentiment Analysis System

## Project Description
This project detects whether a review is Fake (Fraudulent) or Genuine (Legitimate) and also performs Sentiment Analysis on the review.

## Features
- Fake Review Detection using Machine Learning
- Sentiment Analysis (Positive / Negative / Neutral)
- Single Review Analysis
- Batch Review Analysis
- Sentiment Dashboard using Plotly
- Streamlit Web Application

## Technologies Used
- Python
- Machine Learning
- TF-IDF Vectorizer
- Logistic Regression
- Natural Language Processing (NLP)
- Streamlit
- TextBlob
- NLTK
- Plotly

## Machine Learning Models Used
- Naive Bayes
- Support Vector Machine (SVM)
- Logistic Regression

Logistic Regression with TF-IDF gave the best performance, so it is used in deployment.

## How the System Works
1. User enters a review.
2. Text preprocessing is performed (remove stopwords, stemming).
3. TF-IDF converts text into numerical features.
4. Additional features like repeated words, capital letters, and punctuation are extracted.
5. Machine Learning model classifies review as Fake or Genuine.
6. Sentiment analysis is performed using TextBlob.
7. Results are shown in dashboard.

## How to Run the Project
```bash
git clone <your-github-repo-link>
cd AI-Based-Fake-Review-Detection-and-Sentiment-Analysis-System
pip install -r requirements.txt
streamlit run 4.Deployment.py