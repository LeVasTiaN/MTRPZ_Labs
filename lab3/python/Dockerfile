FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "spaceship.main:app", "--host", "0.0.0.0", "--port", "8000"]
