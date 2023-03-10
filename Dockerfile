FROM python:3.9.7-slim

WORKDIR /usr/src/app

COPY . /usr/src/app

RUN apt-get update

RUN pip install -r requirements.txt

RUN pip install python-dotenv

RUN python3 afcdb.py

EXPOSE 5000

ENTRYPOINT [ "python" ] 

CMD [ "app.py" ]