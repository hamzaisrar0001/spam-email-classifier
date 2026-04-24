# Spam Email Classifier

This project is a simple machine learning based spam email classifier. It takes a text message as input and predicts whether the message is spam or not spam.

The purpose of this project is to understand basic natural language processing and machine learning concepts by building a complete end-to-end working system.

---

## How it works

First, the text data is cleaned and preprocessed. This includes converting text to lowercase, removing unnecessary words, and applying basic NLP techniques like tokenization and stemming.

After preprocessing, the text is converted into numerical form using TF-IDF vectorization. Machine learning models cannot work with raw text, so this step converts text into feature vectors.

A trained machine learning model is then used to classify the message as spam or not spam based on the extracted features.

---

## Tools and technologies used

- Python
- Pandas
- NumPy
- Scikit-learn
- NLTK
- Streamlit
- Pickle

---

## Project files

- app.py: Streamlit web application for user input and prediction
- model.pkl: Trained machine learning model
- tfidf.pkl: TF-IDF vectorizer used for text transformation
- requirements.txt: Required dependencies
- Naive_Bayes_classifier.ipynb: Notebook used for training and testing (optional)
- spam.csv: Dataset used for training (optional)

---

## Clone the repository

If you want to run this project on your system, you can clone it using:

git clone https://github.com/hamzaisrar0001/spam-email-classifier.git

---

## How to run

Clone the repository

cd spam-email-classifier

Install dependencies

pip install -r requirements.txt

Run the Streamlit app

streamlit run app.py

---

## Example

Input:
Free entry in a prize draw, claim your reward now

Output:
Spam

---

## Purpose of the project

This project was built for learning purposes. It helps in understanding how machine learning can be applied to text data for classification tasks.

It also gives basic experience in deploying a simple web application using Streamlit.

---

## Future improvements

- Improve accuracy using advanced models
- Use larger dataset
- Improve UI design
- Deploy on cloud platform
