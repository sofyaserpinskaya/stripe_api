FROM python:3.7-slim

RUN mkdir /app

COPY requirements.txt /app

RUN pip3 install -r /app/requirements.txt --no-cache-dir

COPY stripe_api/ /app

WORKDIR /app

CMD ["gunicorn", "stripe_api.wsgi:application", "--bind", "0:8000" ] 