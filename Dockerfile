FROM python:3.10-slim

WORKDIR /app

COPY generate.py ./generate.py

COPY main.py ./main.py

RUN python generate.py
