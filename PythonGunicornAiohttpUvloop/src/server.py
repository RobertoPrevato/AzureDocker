import os
import uvloop
import asyncio
from datetime import datetime
from aiohttp import web


# NB: when running using Gunicorn and aiohttp.worker.GunicornUVLoopWebWorker,
# there is no need to set the uvloop event loop policy
# https://github.com/MagicStack/uvloop/wiki
# asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


_RESP_CACHE = {}


async def index(request):
    size = request.query.get("s")

    if size:
        try:
            page = int(size)
        except ValueError:
            return web.Response(text='Size parameter must be a number', status=400)
        else:
            message = _RESP_CACHE.get(page)
            if message is None:
                message = 'X' * (page * 1000)
                _RESP_CACHE[page] = message
    else:
        a = datetime.now()
        message = "Hello, World from Python 3 with aiohttp, Gunicorn and uvloop! {}".format(a.strftime("%Y-%m-%d %H:%M:%S.%f"))

    return web.Response(text=message)


async def my_web_app():
    app = web.Application()
    app.router.add_get('/', index)
    return app


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    
    app = loop.run_until_complete(my_web_app())
    SERVER_HOST = os.environ.get("SERVER_HOST", "localhost")
    SERVER_PORT = os.environ.get("SERVER_PORT", "8000")

    print("[*] Serving on port: {}".format(SERVER_PORT))

    web.run_app(app, host=SERVER_HOST, port=SERVER_PORT)