FROM python:3.8-slim

WORKDIR .

#COPY main.py .

RUN pip install flask

EXPOSE 5000

CMD ["python", "main.py"]
