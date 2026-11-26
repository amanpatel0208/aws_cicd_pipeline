FROM python:3.8-slim-buster
WORKDIR /app
COPY . /app
RUN apt-get update -y && \
    apt-get install -y awscli && \
    rm -rf /var/lib/api/lists/*
RUN pip install -r requirements.txt
CMD ["python","app.py"]