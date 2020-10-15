# www.srini.tech simple template project with Docker, Flask and GoogleCloud Logging
www.srini.tech simple template project with Docker, Flask and GoogleCloud Logging
If you haven't configured (GCP) google cloud logging , it also prints to console


## Requirements

* Docker Compose 1.21.2+
* Python 3.6 +

## Run with Docker Compose

```bash
# building the container
sudo docker-compose build

# starting up a container
sudo docker-compose up
```

## Build the virtual environment

```bash
virtualenv -p /usr/bin/python3.6 venv
source venv/bin/activate
pip3 install -r requirements.txt
pip3 install -r test-requirements.txt
```

## Simple Get api Health Check

```http
http://localhost:8082/hello
```

## Simple Get api json list of Tasks

```http
http://localhost:8082/tasks
```

## Simple Get api - Square a number

```http
http://localhost:8082/square?number=3
```

## To Integrate with Google Cloud Logging

Put your *.json file in <project root> folder
and specify path in /basic/config/__init__.py file

Ex.os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './xyz.json'

