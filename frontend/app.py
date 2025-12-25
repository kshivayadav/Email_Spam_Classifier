import streamlit as st
import requests

st.set_page_config(page_title="SMS Spam Classifier", page_icon="📩", layout="wide")

st.title("📩 SMS Spam Classifier")
st.write("This app uses **NLP + Machine Learning** to classify SMS messages as Spam or Not Spam.")


st.sidebar.title("About Project")
st.sidebar.info(
    "This SMS Spam Classifier was built using **NLTK, Scikit-learn, and Streamlit**. "
    "It preprocesses text, vectorizes it, and predicts using a trained ML model."
)
API_URL = "http://backend:8000/predict"
input_sms = st.text_area('Enter your message')
if st.button('predict'):
    if input_sms.strip() == "":
        st.warning("⚠️ Please enter a message before predicting.")
    else:
        try:
            result = requests.post(API_URL,json = {"message":input_sms},timeout=5)
            print(result)
            result.raise_for_status()
            response = result.json()
            print(response)

            if response['prediction'] == "Spam":
                st.error(f"🚨 Spam detected!\n\n**Message:** {input_sms}")
            else:
                st.success(f"✅ Not Spam\n\n**Message:** {input_sms}")
        except requests.exceptions.ConnectionError:
            st.error("❌ Could not connect to FastAPI backend. Is it running?")
        except requests.exceptions.Timeout:
            st.error("⏳ Request timed out. Try again.")
        except requests.exceptions.HTTPError as http_err:
            st.error(f"⚠️ Backend returned an error: {http_err}")
        except Exception as e:
            st.error(f"Unexpected error: {e}")



