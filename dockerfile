FROM python:3.8-slim-buster
FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir awscli
RUN pip install -r requirements.txt
CMD ["python","app.py"]
