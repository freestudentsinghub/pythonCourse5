FROM python:3.12-slim

WORKDIR /app

RUN pip install poetry
RUN poetry config virtualenvs.create false
COPY pyproject.toml ./
RUN poetry install --no-root

COPY . .
