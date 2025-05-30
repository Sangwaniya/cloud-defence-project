FROM python:3.12.10-alpine3.21

WORKDIR /app/

COPY . .

RUN pip install -r ./requirements.txt


CMD ["python3", "-u", "leaker.py"]