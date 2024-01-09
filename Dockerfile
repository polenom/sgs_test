
FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1
ENV PATH="/root/.local/bin:${PATH}"
WORKDIR /app

COPY . /app

RUN pip install poetry
RUN poetry self update
RUN poetry install
