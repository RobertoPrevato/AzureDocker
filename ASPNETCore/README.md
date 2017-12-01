# NET Core 2.0 ASP.NET Core applications
This folder is a project template for NET Core 2.0 web applications powered by ASP.NET Core and Kestrel.

## Publishing in Azure Container Registry
To publish a Docker image in [Azure Container Registry](https://docs.microsoft.com/en-us/azure/container-registry/container-registry-get-started-portal):

```
docker login --username <username> --password <password> <login server>

docker tag IMAGE_NAME <login server>/IMAGE_NAME:TAG

docker push <login server>/IMAGE_NAME:TAG
```