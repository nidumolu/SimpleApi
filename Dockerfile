FROM python:3.7.9-slim-stretch


RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt --upgrade

COPY . /usr/src/app

ENTRYPOINT [ "python" ]
CMD ["basic/simpleApi.py"]


