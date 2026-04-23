import streamlit as st
import pickle

# Load trained model + tfidf (assume saved already)
tfidf = pickle.load(open("tfidf.pkl", "rb"))
nb = pickle.load(open("model.pkl", "rb"))

st.title("📧 Spam Email Classifier")
st.write("Enter email text and check if it's Spam or Ham")

user_input = st.text_area("Enter Email Text")

if st.button("Predict"):
    if user_input:
        transformed = tfidf.transform([user_input])
        result = nb.predict(transformed)

        if result[0] == 1:
            st.error("🚨 Spam Email 🚨")
        else:
            st.success("✅ Ham (Not Spam) Email")