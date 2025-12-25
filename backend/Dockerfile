FROM python:3.10-slim

# 1. Set base working directory inside container
WORKDIR /app

# 2. Copy backend requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 3. Copy FastAPI application folder (appp)
COPY appp ./appp

# 4. Switch working directory to FastAPI app folder
WORKDIR /app/appp

# 5. Expose FastAPI port
EXPOSE 8000

# 6. Start FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

