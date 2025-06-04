#  AI Sentiment Dashboard

A simple yet powerful AI dashboard built with **Streamlit** and **Hugging Face Transformers**, designed to analyze sentiment from custom input or live news headlines.

---

##  Features

-  Sentiment Analysis using `distilbert-base-uncased-finetuned-sst-2-english`
-  Fetches top headlines via News API (country-selectable)
-  Sidebar for full control:
  - Country selection
  - Headline limit
  - Toggle charts
  - Custom title
-  Dark theme for a sleek UI
-  History logging of analyzed text
-  Interactive chart of sentiment distribution
-  Clear buttons for input and history

---

##  Demo

![Dashboard Screenshot](screenshot.png) <!-- Replace with your actual screenshot if available -->

---

##  Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/your-username/sentiment-dashboard.git
cd sentiment-dashboard
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

Make sure you have **PyTorch** or **TensorFlow** installed for the model to run.

### 3. Add `.streamlit/config.toml` for dark mode (optional)

```toml
[theme]
base = "dark"
primaryColor = "#4CAF50"
backgroundColor = "#0e1117"
secondaryBackgroundColor = "#262730"
textColor = "#FAFAFA"
font = "sans serif"
```

### 4. Add your News API key

Open `app.py` and replace:

```python
NEWS_API_KEY = "your_api_key_here"
```

Get a key from: [https://newsapi.org/](https://newsapi.org/)

### 5. Run the app

```bash
streamlit run app.py
```

---

##  Project Structure

```
sentiment-dashboard/
│
├── app.py
├── requirements.txt
├── .streamlit/
│   └── config.toml
└── README.md
```

---

##  To-Do / Ideas

* [ ] Export sentiment history to CSV
* [ ] Add emotion classification model
* [ ] Deploy on Streamlit Cloud
* [ ] Add logo and favicon

---

##  License

MIT License. Feel free to fork and remix!

---

##  Author

Built by [Yitbarek Geletaw](https://github.com/emegua19) — powered by caffeine & curiosity

