FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["dagster", "api", "grpc", "-m", "apod_pipeline", "--port", "4000"]
