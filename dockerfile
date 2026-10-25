FROM python:3.13-slim
WORKDIR /hivebox
COPY version.txt .
COPY app/ app/
CMD [ "python3", "app/main.py" ]
