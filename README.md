# AzureDocker
Docker images for web applications to host in Azure.

![All machines deployed in Azure](https://robertoprevato.github.io/images/posts/azuredocker/azure-tutorial-rg-demo-apps.png)

| Image   | Description |
|---------|-------------|
| ASPNETCore | ASP.NET Core web application, using .NET Core 2.0 |
| GoHttp | Go 1.9.1 web application, using net/http |
| GoFastHttp | Go 1.9.1 web application, using fast http |
| PyPyGunicornGeventFlask | PyPy 3, Gunicorn, Gevent, Flask web application |
| PythonUvloopHttpTools | Python 3.6.2 application using uvloop and httptools |

---

The preparation of these images has been described in this blog post: [https://robertoprevato.github.io/Running-Docker-applications-in-Azure/](https://robertoprevato.github.io/Running-Docker-applications-in-Azure/).

Applications templates are ready to support benchmarks, returning two kinds of answer:
* an Hello World message with a timestamp and description of the technology stack
* given a query parameter `s` with numeric value `n` between 1 and 100, a response of _n kB_, using cached variables for these messages

This is inspired and partially reproduced from the code prepared by [MagicStack](https://github.com/MagicStack) for their benchmarks.