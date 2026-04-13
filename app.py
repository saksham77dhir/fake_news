import streamlit as st
import pickle
import re
from nltk.corpus import stopwords
import nltk

# download stopwords (runs once)
nltk.download('stopwords')

# load model and vectorizer
model = pickle.load(open("fake_news_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# stopwords
stop_words = set(stopwords.words('english'))

# cleaning function (same as training)
def clean_text(content):
    content = re.sub('[^a-zA-Z]', ' ', content).lower().split()
    return ' '.join(word for word in content if word not in stop_words)

# UI
st.title("📰 Fake News Detection App")

st.write("Enter a news article below to check if it is Fake or Real.")

input_text = st.text_area("Enter News Text")

if st.button("Predict"):
    if input_text.strip() == "":
        st.warning("Please enter some text")
    else:
        # preprocess
        cleaned_text = clean_text(input_text)

        # vectorize
        vector_input = vectorizer.transform([cleaned_text])

        # predict
        prediction = model.predict(vector_input)

        # output
        if prediction[0] == 0:
            st.success("✅ This is Real News")
        else:
            st.error("❌ This is Fake News")