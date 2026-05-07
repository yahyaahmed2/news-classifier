import streamlit as st
import joblib
import re

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-zA-Z]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


model = joblib.load("final_best_model.pkl")

label_map = {
    1: "World/Political",
    2: "Sports",
    3: "Business",
    4: "Sci/Tech"
}

st.title("📰 News Classifier")

text = st.text_area("Enter news text:")

if st.button("Predict"):
    if text.strip():
        cleaned_text = clean_text(text)
        pred = model.predict([cleaned_text])[0]
        st.success(f"Prediction: {label_map[pred]}")
    else:
        st.warning("Please enter text")