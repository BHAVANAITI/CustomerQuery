FROM ubuntu:latest
MAINTAINER 1503012 "1503012@ritindia.edu"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install chatterbot
EXPOSE 8080
ENTRYPOINT ["python"]
CMD ["app.py"]
