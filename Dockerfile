FROM python:3.7-alpine
RUN pip install flask==1.1.1
COPY . /app
WORKDIR /app
ENTRYPOINT ["python"]
CMD ["app.py"]
