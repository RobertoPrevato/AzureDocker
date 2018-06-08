#!/bin/sh
# gunicorn --name 'Gunicorn uvicorn app' --chdir /app/src --bind 0.0.0.0:$SERVER_PORT server:my_web_app --worker-class aiohttp.GunicornWebWorker --workers $GUWORKERS
cd /app/src
uvicorn app:TestApp -c uvicorn_conf.py