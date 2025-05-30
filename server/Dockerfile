FROM python:3.12-alpine
WORKDIR /app
COPY log_server.py .
RUN pip install flask
CMD ["python3", "-u", "log_server.py"]