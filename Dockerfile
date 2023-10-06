FROM python:3.11

WORKDIR /

COPY . .

RUN apt-get -y update
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install -r req.txt

CMD pyttman runclient discorddoogie