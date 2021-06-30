FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "src.main.server:app", "--host", "0.0.0.0", "--port", "80"]
