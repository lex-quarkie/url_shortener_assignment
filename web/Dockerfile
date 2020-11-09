FROM python:3.8.6-slim-buster
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /
COPY ./app /app

RUN pip install --no-cache-dir  -r  requirements.txt && pip install gunicorn
ENTRYPOINT ["/runserver.sh"]