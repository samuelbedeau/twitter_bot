FROM python:3.7-alpine

COPY bots/config.py /bots/
COPY bots/fav.py /bots/
COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

WORKDIR /bots
CMD ["python3", "fav.py"]

