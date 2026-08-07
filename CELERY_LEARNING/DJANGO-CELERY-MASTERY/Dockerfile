FROM python:3.13-slim

WORKDIR /django

#ensures that python output is sent directly to the terminal without bufffering 
ENV PYTHONUNBUFFERED=1
#prevent python from writin .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

RUN pip install  --upgrade pip

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . ./django



