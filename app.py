import streamlit as st
import pickle
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps=PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = [word for word in text.split()]
    text = [word for word in text if word.isalnum()]
    text = [word for word in text if word not in stopwords.words('english') and word not in string.punctuation]
    y = []
    for word in text:
        y.append(ps.stem(word))
    return " ".join(y)

tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

st.title('Sms Spam Classifier')
input_sms = st.text_area('Enter your message')
if st.button('predict'):
    # 1 preprocess
    transformed_sms = transform_text(input_sms)
    # 2 vectorize
    vector_input = tfidf.transform([transformed_sms])
    # 3 predict
    result = model.predict(vector_input)[0]
    # 4 Display
    if result == 1:
        st.header('Spam Sms')
    else:
        st.header('Not Spam')