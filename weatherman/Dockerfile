FROM python:3.12.10-alpine3.21

WORKDIR /app/

COPY weatherman.py .

RUN pip install requests

CMD ["python3", "-u", "weatherman.py"] 