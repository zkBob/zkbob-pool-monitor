FROM python:3.9-alpine

RUN apk update && apk upgrade

RUN python -m pip install --upgrade pip
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

# Remove cache.
RUN python -m pip cache purge

WORKDIR /app

COPY main.py .
COPY graphql_schemas graphql_schemas
COPY monitors monitors
COPY settings settings
COPY slack slack
COPY thegraph thegraph
COPY utils utils

# default endpoint
ENTRYPOINT python main.py