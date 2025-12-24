import pickle

try:
    with open("vectorizer.pkl", "rb") as f:
        tfidf = pickle.load(f)
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
except FileNotFoundError as fnf:
    raise RuntimeError(f"Model files not found: {fnf}")
except Exception as e:
    raise RuntimeError(f"Error loading model/vectorizer: {e}")

