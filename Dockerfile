FROM ubuntu:latest
MAINTAINER 1503012 "1503012@ritindia.edu"
RUN apt-get update -y
RUN apt-get install curl
RUN curl -fsSL https://get.docker.com | sh
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install chatterbot 
RUN pip install flask 
RUN pip install render 
Run pip install render_template
EXPOSE 8080
ENTRYPOINT ["python"]
CMD ["app.py"]

