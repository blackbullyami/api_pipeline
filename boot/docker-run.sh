#!/bin/bash

cd /code

RUN_PORT=${PORT:-8000}
RUN_HOST=${HOST:-0.0.0.0}

exec gunicorn main:app \
    --workers 4 \
    --worker-class uvicorn.workers.UvicornWorker \
    --bind ${RUN_HOST}:${RUN_PORT}
