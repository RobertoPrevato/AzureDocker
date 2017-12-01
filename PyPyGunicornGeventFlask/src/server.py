import os
from datetime import datetime
from flask import Flask, request
from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__)

app.wsgi_app = ProxyFix(app.wsgi_app)

flask_debug = os.environ.get("FLASK_DEBUG", False)

app.config.update({"DEBUG": bool(flask_debug)})


_RESP_CACHE = {}
plain_text = {"Content-Type": "text/plain"}


@app.route("/")
def index():
    page = request.args.get("s")
    if not page:
        a = datetime.now()
        return "Hello, World from PyPy 3, Gunicorn and Gevent! {}".format(a.strftime("%Y-%m-%d %H:%M:%S.%f"))

    try:
        page = int(page)
    except ValueError:
        return ("Invalid query: cannot parse size", 400, plain_text)

    if page > 101:
        return ("Invalid query: exceeds 101", 400, plain_text)

    message = _RESP_CACHE.get(page)
    if message is None:
        message = b'X' * (page * 1000)
        _RESP_CACHE[page] = message
    return (message, 200, plain_text)

# Following code is executed when running the server directly, for development
if __name__ == "__main__":
    # NB: for the server port, read an environmental variable called "SERVER_PORT", or use a default value
    SERVER_PORT = os.environ.get("SERVER_PORT", "8000")
    app.run(host="", port=int(SERVER_PORT))