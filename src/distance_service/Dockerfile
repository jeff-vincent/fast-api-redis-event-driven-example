FROM python:3.10
COPY ./src/redis.py .
COPY ./src/distance_service/ . 
RUN pip install -r requirements.txt
CMD python distance.py