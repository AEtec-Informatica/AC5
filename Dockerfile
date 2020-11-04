FROM ubuntu:mais recente
RUN apt-get update -y
RUN apt-get install -y python3-pip python-dev build-essential
COPY . 
WORKDIR /
RUN pip3 install -- no-cacha-dir -r requirements.txt
CMD ["python3", "setup.py"]
