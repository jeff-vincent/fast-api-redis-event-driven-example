FROM python:3.9
COPY ./src/redis.py .
COPY ./src/mongo.py .
COPY ./src/email_service/ . 
RUN pip install -r requirements.txt
CMD python email.py