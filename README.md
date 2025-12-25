### 📨 SMS Spam Classifier

A full-stack, Dockerized SMS Spam Classifier using Machine Learning, FastAPI, and Streamlit.
Provides a web interface to classify SMS messages as spam or ham, with a REST API backend for predictions.

🛠️ Project Structure

sms_spam_classifier/

│
├── backend/

│   ├── appp/               # FastAPI application

│   │   ├── main.py         # API entrypoint

│   │   ├── prediction.py   # Prediction logic

│   │   ├── ml_model.py     # ML model loading

|   |   ├── model.pkl       # Trained ML model

|   |   ├── vectorizer.pkl  # Vectorizer for text preprocessing

│   │   └── schema.py       # Pydantic request/response models

│   ├── Dockerfile          # Backend Dockerfile

│   └── requirements.txt    # Python dependencies

│

├── frontend/

│   ├── app.py              # Streamlit frontend

│   ├── Dockerfile          # Frontend Dockerfile

│   └── requirements.txt    # Python dependencies

├── docker-compose.yml      # Compose file for full system

└── README.md

⚙️ Features

FastAPI backend serving ML model predictions.

Streamlit frontend UI for interactive SMS classification.

Dockerized backend and frontend for reproducible deployment.

Docker Compose for orchestrating frontend and backend.

Health check endpoint (/health) for backend monitoring.

Supports local and production deployment.

💻 Installation & Run Locally (Without Docker)

Clone the repository:
```
git clone https://github.com/kshivayadav/Email_Spam_Classifier
cd sms_spam_classifier
```

Create a virtual environment and activate:
```
python -m venv .venv
source .venv/bin/activate       # Linux / Mac
.venv\Scripts\activate          # Windows
```

Install backend dependencies:
```
pip install -r backend/requirements.txt
```

Run FastAPI backend:
```
uvicorn backend.appp.main:app --reload --host 0.0.0.0 --port 8000
```

Run Streamlit frontend:
```
streamlit run frontend/app.py
```

Open frontend in browser:
```
http://localhost:8501
```

Open backend Swagger docs:
```
http://localhost:8000/docs
```

🐳 Dockerized Run

Build & Run Backend
```
docker build -t sms-backend ./backend
docker run -p 8000:8000 sms-backend
```

Build & Run Frontend
```
docker build -t sms-frontend ./frontend
docker run -p 8501:8501 sms-frontend
```

Run Both with Docker Compose
```
docker-compose up --build
```

Frontend available at:
```
http://localhost:8501
```

Backend Swagger docs:
```
http://localhost:8000/docs
```

🌐 API Endpoints

Endpoint	Method	Description
/predict	POST	Classify SMS messages (spam/ham)
/health	GET	Health check for backend service



🔧 Technologies Used

Python 3.10

FastAPI – REST API backend

Streamlit – Frontend UI

scikit-learn – ML model

NLTK – Text preprocessing

Docker – Containerization

Docker Compose – Multi-service orchestration

🎯 Future Improvements

Add authentication to API endpoints.

Deploy on cloud platforms like AWS, Render, or Railway.

Support batch SMS classification.

Add model retraining pipeline.

📜 License

MIT License © K Shiva Kumar
