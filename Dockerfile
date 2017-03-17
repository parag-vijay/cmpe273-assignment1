From python:2.7.13
MAINTAINER Parag Vijayvergia "vijay.parag9@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install  -r  requirements.txt
ENTRYPOINT ["python", "app.py"]
