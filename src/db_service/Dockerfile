FROM python:3.10
COPY ./src/redis.py .
COPY ./src/mongo.py .
COPY ./src/db_service/ .
RUN pip install -r requirements.txt
CMD python db.py