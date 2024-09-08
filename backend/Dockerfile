FROM python:3.9-slim-buster

ENV PYTHONUNBUFFERED=1

# Install make and other necessary packages
RUN apt-get update && apt-get install -y make gcc build-essential --no-install-recommends

WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]