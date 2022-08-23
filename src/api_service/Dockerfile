FROM python:3.10
COPY ./src/redis.py .
COPY ./src/api_service/ . 
RUN pip install -r requirements.txt
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]