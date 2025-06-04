import streamlit as st
from transformers import pipeline
import pandas as pd
import requests
import plotly.express as px

classifier = pipeline(
    "sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english",
    revision="714eb0f"
)

# ------------------------------
# Theme & Page Config
# ------------------------------
st.set_page_config(page_title="Sentiment Dashboard", layout="wide")

# Set custom title from sidebar
st.sidebar.title("⚙️ Settings")

custom_title = st.sidebar.text_input("App Title", "AI Sentiment Dashboard")
st.title(custom_title)

# ------------------------------
# idebar Controls
# ------------------------------
country = st.sidebar.selectbox("News Country", options=["us", "gb", "ca", "au", "in"], index=0)
num_headlines = st.sidebar.slider(" Number of Headlines", 5, 20, 10)
show_chart = st.sidebar.checkbox(" Show Sentiment Chart", value=True)
clear_history = st.sidebar.button("🧹 Clear All History")

# ------------------------------
# Load Sentiment Pipeline
# ------------------------------
@st.cache_resource
def load_classifier():
    return pipeline("sentiment-analysis")
classifier = load_classifier()

# ------------------------------
# Session State
# ------------------------------
if clear_history:
    st.session_state.history = []

if "history" not in st.session_state:
    st.session_state.history = []

# ------------------------------
# Custom Sentence Input
# ------------------------------
with st.container():
    st.subheader(" Analyze a Sentence")
    col1, col2 = st.columns([4, 1])
    with col1:
        text = st.text_input("Enter a sentence:")
    with col2:
        if st.button("Clear Input"):
            st.experimental_rerun()

    if text:
        result = classifier(text)[0]
        st.success(f"**Label:** {result['label']} | **Confidence:** {result['score']:.2f}")
        st.session_state.history.append({
            "Type": "Custom Input",
            "Text": text,
            "Label": result['label'],
            "Score": round(result['score'], 2)
        })

# ------------------------------
# Live News Headlines
# ------------------------------
st.markdown("---")
st.subheader(" Live News Sentiment")

NEWS_API_KEY = "your_api_key_here"  # Replace with your real API key

def get_news(country="us", limit=10):
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "country": country,
        "apiKey": NEWS_API_KEY,
        "pageSize": limit
    }
    res = requests.get(url, params=params)
    return [a["title"] for a in res.json().get("articles", []) if a.get("title")]

if st.button("Fetch & Analyze News"):
    headlines = get_news(country, num_headlines)
    results = [{"Type": "News", "Text": h, **classifier(h)[0]} for h in headlines]
    for r in results:
        r["Score"] = round(r["score"], 2)
        del r["score"]
    st.session_state.history.extend(results)

# ------------------------------
# Display History
# ------------------------------
st.markdown("---")
st.subheader("Sentiment History")

if st.session_state.history:
    df = pd.DataFrame(st.session_state.history)
    st.dataframe(df, use_container_width=True)

    if show_chart:
        chart = px.histogram(df, x="Label", color="Type", title="Sentiment Distribution")
        st.plotly_chart(chart, use_container_width=True)
else:
    st.info("No data yet. Try analyzing a sentence or fetching news.")

