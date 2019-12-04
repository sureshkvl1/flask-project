FROM python:3.7-alpine
RUN pip install flask==1.1.1
#RUN apt-get update -y
#RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
#RUN pip install flask==0.12
ENTRYPOINT ["python"]
CMD ["app.py"]
