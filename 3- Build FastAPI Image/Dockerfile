FROM python:3.8

RUN mkdir /code

WORKDIR /code  

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY  . .

CMD ["uvicorn","main:app","--host=0.0.0.0","--port=8080"]

# docker build -t fastapi .
# docker run -p 8080:8080 --name new-fastapi fastapi

