# syntax=docker/dockerfile:1

FROM python

RUN apt-get -y update && apt-get -y upgrade && apt-get install -y --no-install-recommends ffmpeg

WORKDIR /docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

RUN mkdir -p /docker/app/input
RUN mkdir -p /docker/app/output
RUN mkdir -p /docker/app/temp

COPY . .
CMD ["python3", "app/main.py"]
