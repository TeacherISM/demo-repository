FROM python:3.7-stretch

RUN mkdir /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
COPY src/ /app

WORKDIR /app/
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
