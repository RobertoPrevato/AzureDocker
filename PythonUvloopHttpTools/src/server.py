import os
import sys
import asyncio
import httptools
import uvloop
from datetime import datetime

from socket import *


class HttpRequest:
    __slots__ = ('_protocol', '_url', '_headers', '_version')

    def __init__(self, protocol, url, headers, version):
        self._protocol = protocol
        self._url = url
        self._headers = headers
        self._version = version


class HttpResponse:
    __slots__ = ('_protocol', '_request', '_headers_sent')

    def __init__(self, protocol, request):
        self._protocol = protocol
        self._request = request
        self._headers_sent = False

    def write(self, data):
        #
        # TODO: implement here your logic to handle different response types
        # e.g. if not found, return status 404; etc.
        #
        self._protocol._transport.write(b''.join([
            'HTTP/{} 200 OK\r\n'.format(self._request._version).encode('latin-1'),
            b'Content-Type: text/plain\r\n',
            'Content-Length: {}\r\n'.format(len(data)).encode('latin-1'),
            b'\r\n',
            data
        ]))


class HttpProtocol(asyncio.Protocol):

    __slots__ = ('_loop',
                 '_transport', '_current_request', '_current_parser',
                 '_current_url', '_current_headers')

    def __init__(self, *, loop=None):
        if loop is None:
            loop = asyncio.get_event_loop()
        self._loop = loop
        self._transport = None
        self._current_request = None
        self._current_parser = None
        self._current_url = None
        self._current_headers = None

    def on_url(self, url):
        self._current_url = url

    def on_header(self, name, value):
        self._current_headers.append((name, value))

    def on_headers_complete(self):
        self._current_request = HttpRequest(
            self, self._current_url, self._current_headers,
            self._current_parser.get_http_version())

        self._loop.call_soon(
            self.handle, self._current_request,
            HttpResponse(self, self._current_request))

    def connection_made(self, transport):
        self._transport = transport
        sock = transport.get_extra_info('socket')
        try:
            sock.setsockopt(IPPROTO_TCP, TCP_NODELAY, 1)
        except (OSError, NameError):
            pass

    def connection_lost(self, exc):
        self._current_request = self._current_parser = None

    def data_received(self, data):
        if self._current_parser is None:
            assert self._current_request is None
            self._current_headers = []
            self._current_parser = httptools.HttpRequestParser(self)

        self._current_parser.feed_data(data)

    def handle(self, request, response):
        parsed_url = httptools.parse_url(self._current_url)
        
        a = datetime.now()
        #
        # TODO: implement here your logic to handle responses by router, etc.
        # 
        resp = "Hello World, from Python 3.6.2, uvloop and httptools! {}".format(a.strftime("%Y-%m-%d %H:%M:%S.%f"))

        response.write(resp.encode("utf8"))
        if not self._current_parser.should_keep_alive():
            self._transport.close()
        self._current_parser = None
        self._current_request = None


def abort(msg):
    print(msg, file=sys.stderr)
    sys.exit(1)


def httptools_server(loop, addr):
    return loop.create_server(lambda: HttpProtocol(loop=loop), *addr)


if __name__ == "__main__":
    SERVER_PORT = os.environ.get("SERVER_PORT", "44555")

    loop = uvloop.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.set_debug(False)
    
    server_factory = httptools_server

    addr = ("0.0.0.0", int(SERVER_PORT))

    server = loop.run_until_complete(server_factory(loop, addr))
    print('[*] Starting uvloop httptools on: {}'.format(addr))

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        print("[*]")
        print("[*] User interrupted")
        print("[*]")
    finally:
        server.close()
        loop.close()