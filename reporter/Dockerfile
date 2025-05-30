FROM python:3.12.10-alpine3.21

WORKDIR /app/

COPY . .

RUN pip install requests

CMD ["python3", "-u", "reporter.py"]  
# run Python in unbuffered mode so logs appear immediately