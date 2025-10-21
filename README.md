**🚀 Project Overview**

This project applies Natural Language Processing (NLP) and Machine Learning techniques to automatically detect spam in text messages or emails.
The app allows users to input any message and instantly get a prediction through a simple, interactive Streamlit web interface.


**🧠 Features**

📩 Real-time text classification (Spam / Not Spam)

🔍 Text cleaning, tokenization, stopword removal, and stemming

🧮 TF-IDF Vectorization for feature extraction

🤖 Model trained using Multinomial Naïve Bayes

🌐 Deployed using Streamlit for easy access


**📂 Project Structure**
Email_Spam_Classifier/
│
├── Email_spam_classifier.ipynb   # Notebook for data analysis and model training  
├── app.py                        # Streamlit app for deployment  
├── spam_model.pkl                # Saved trained model  
├── vectorizer.pkl                # Saved TF-IDF vectorizer  
├── requirements.txt              # Dependencies list  
└── README.md                     # Project documentation  


**⚙️ Tech Stack**

Languages: Python

Libraries:

pandas, numpy, matplotlib, seaborn

scikit-learn

nltk

streamlit

pickle

**🧩 Model Building Process**

1. Data Preprocessing

Loaded dataset spam.csv

Dropped unnecessary columns and renamed v1 → target, v2 → text

Encoded labels (ham → 0, spam → 1)

Text cleaning pipeline:

Convert to lowercase

Remove special characters and punctuation

Tokenize text

Remove stopwords

Apply stemming using PorterStemmer

2. Feature Extraction

Used TF-IDF Vectorizer to convert text into numerical features

3. Model Training

Algorithm used: Multinomial Naïve Bayes

Evaluation metrics: Accuracy, Precision, Recall, F1-score

Model achieved high precision and accuracy on test data

4. Deployment

Model serialized using pickle

Deployed as an interactive web app with Streamlit

**💻 Run Locally**

Clone the Repository
git clone https://github.com/kshivayadav/Email_Spam_Classifier.git
cd Email_Spam_Classifier

Install Dependencies
pip install -r requirements.txt

Run the App
streamlit run app.py

Open in Browser
http://localhost:8501


**📊 Results
**
Achieved ~97–98% accuracy on validation data

Reliable spam detection with high recall and precision

**🧠 Future Work**

Integrate deep learning models (LSTM / BERT)

Support multiple languages

Add an API endpoint for integration with messaging systems

**🤝 Contributing**

Contributions are welcome!
Feel free to fork, improve, and submit a pull request.
