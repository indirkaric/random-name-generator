FROM python:3.10.4

ADD . /code
WORKDIR /code

CMD ["python", "main.py"]
