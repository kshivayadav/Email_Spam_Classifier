from http.client import HTTPException
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps=PorterStemmer()
from ml_model import tfidf,model



try:
    nltk.download("stopwords")
except Exception as e:
    print(f"Warning: Could not download stopwords: {e}")


def transform_text(text):
    try:
        text = text.lower()
        text = [word for word in text.split()]
        text = [word for word in text if word.isalnum()]
        text = [word for word in text if word not in stopwords.words('english') and word not in string.punctuation]
        y = []
        for word in text:
            y.append(ps.stem(word))
        return " ".join(y)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Text preprocessing failed: {e}")


def prediction(input_sms):
    try:
        if not input_sms.strip():
            raise HTTPException(status_code=400, detail="Message cannot be empty")
        transformed_sms = transform_text(input_sms)
        vector_input = tfidf.transform([transformed_sms])
        response = model.predict(vector_input)[0]
        return response
    except HTTPException as http_err:
        raise http_err
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {e}")
