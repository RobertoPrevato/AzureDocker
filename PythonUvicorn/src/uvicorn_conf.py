import os
import multiprocessing

workers = multiprocessing.cpu_count()

SERVER_PORT = os.environ.get('SERVER_PORT', '8080')

bind = "0.0.0.0:" + SERVER_PORT
keepalive = 120
errorlog = '-'
pidfile = '/tmp/uvicorn.pid'