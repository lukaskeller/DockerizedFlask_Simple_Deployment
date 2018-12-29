FROM python:3.6.6-stretch

MAINTAINER Lukas Keller

RUN pip install gunicorn

COPY requirements.txt /

RUN pip install -r requirements.txt

COPY . /app
WORKDIR /app

CMD ["gunicorn", "app.wsgi:app", "--bind", "0.0.0.0:5000", "--workers", "3" ]



