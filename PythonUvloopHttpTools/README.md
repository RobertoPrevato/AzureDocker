# Python 3.6.2 application using uvloop and httptools
This folder is a project template for CPython 3.6> web applications powered by asyncio, [uvloop](https://github.com/MagicStack/uvloop) and [httptools](https://github.com/MagicStack/httptools).

uvloop is, to use the words of its authors, an "ultra fast implementation of asyncio event loop on top of libuv". It is indeed fast. httptools is a barebone, fast HTTP parser, implemented by same people. For more information on this interesting technology, see:
* [
uvloop: Blazing fast Python networking, by by Yury Selivanov - May 03, 2016](https://magic.io/blog/uvloop-blazing-fast-python-networking/)
* [https://github.com/MagicStack](https://github.com/MagicStack)

The Python code of this image (`server.py`) is a modification of source code found in: [https://github.com/MagicStack/vmbench](https://github.com/MagicStack/vmbench).

## Note
To develop locally, you will need to install latest version of Python and use the right interpreter when creating a virtual environment for the project.
For example, under Ubuntu, assuming that PATH variable is default and CPython 3.6.2 was installed:

```bash
/opt/python3.6.2/bin/python3 -m venv env
```