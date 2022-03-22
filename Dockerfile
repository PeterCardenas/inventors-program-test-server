FROM python:3

COPY ./ /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENV FLASK_APP="app"
ENV FLASK_ENV="production"

