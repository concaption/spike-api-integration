FROM python:3.10.4-buster

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "5000"]
