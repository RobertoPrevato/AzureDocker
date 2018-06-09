#!/bin/sh
gunicorn --name 'Gunicorn aiohttp app' --chdir /app/src --bind 0.0.0.0:$SERVER_PORT server:my_web_app --worker-class aiohttp.worker.GunicornUVLoopWebWorker --workers $GUWORKERS