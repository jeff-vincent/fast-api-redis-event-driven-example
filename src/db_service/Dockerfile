FROM python:3.10
COPY ../redis.py .
COPY ../mongo.py .
COPY . .
RUN pip install -r requirements.txt
CMD python db.py