FROM ubuntu:22.04

RUN apt-get update && apt-get install -y python3 python3-pip

RUN apt install -y python3-requests

WORKDIR /app

COPY logger.py .

CMD ["python3", "logger.py"]
