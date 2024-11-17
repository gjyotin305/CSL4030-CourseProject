FROM python:3.10-slim

WORKDIR /app

RUN pip install spacy fastapi uvicorn loguru
RUN python -m spacy download en_core_web_sm

COPY . .

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]