# Base image being derived from Python
FROM python:3.7-alpine

# Copy files into from dir into container
COPY bots/config.py /bots/
COPY bots/fav.py /bots/
COPY requirements.txt /tmp
# Install pip dependencies for python scripts 
RUN pip install -r /tmp/requirements.txt

# Set directory to work from 
WORKDIR /bots

# Starting point command for container
CMD ["python3", "fav.py"]

