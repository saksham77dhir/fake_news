# 📰 Fake News Detection using Machine Learning

A Machine Learning project that classifies news articles as **Fake or Real** using Natural Language Processing (NLP) techniques and Logistic Regression. The project also includes a **Streamlit web app** for real-time predictions.

---

## 🚀 Features

* Text preprocessing using NLP techniques
* Stopwords removal and text cleaning
* TF-IDF vectorization
* Logistic Regression model for classification
* Interactive Streamlit web app
* Real-time prediction of news authenticity

---

## 🧠 Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* NLTK
* Streamlit

---

## 📂 Project Structure

```
Fake-News-Detection/
│
├── app.py                  # Streamlit app
├── fake_news_model.pkl     # Trained ML model
├── vectorizer.pkl          # TF-IDF vectorizer
├── Fake.csv                # Fake news dataset
├── True.csv                # Real news dataset
├── fake_news.ipynb         # Model training notebook
├── requirements.txt        # Dependencies
└── README.md               # Project documentation
```


## 🧪 How It Works

1. Input news text in the app
2. Text is cleaned (removal of special characters & stopwords)
3. TF-IDF converts text into numerical features
4. Logistic Regression predicts whether news is **Fake or Real**

---

## 📊 Model Performance

* Training Accuracy: ~98–100%
* Testing Accuracy: ~95–98%

*(May vary depending on data split)*

---

## 📌 Example

**Input:**

```
Scientists discover new method to improve battery efficiency.
```

**Output:**

```
Real News ✅
```

---

## 🎯 Future Improvements

* Use advanced models (LSTM, BERT)
* Deploy on cloud (Streamlit Cloud / Render)
* Improve dataset quality and size
* Add news source credibility features

---


🚀 Live Demo

🔗 http://fakenews-hyper7.streamlit.app/

