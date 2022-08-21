FROM python:3.10
COPY ../redis.py .
COPY . . 
RUN pip install -r requirements.txt
CMD python api.py