## How to deploy using Azure CLI

Create variables, to avoid repetition
```bash
export APPNAME=gohttp
export RGNAME=${APPNAME}-dev-euw-rg
```

Create resource group
```bash
az group create --name $RGNAME --location "westeurope"
```

Deploy application inside this resource group
```bash
az group deployment create --name example --resource-group $RGNAME --template-file azuredeploy.json --parameters azuredeploy.parameters.json
```

Given ARM template already works with public container registered in Docker Hub.

Configure Web App to use Docker container from Docker Hub
https://hub.docker.com/r/robertoprevato/flask/
```bash
az webapp config container set --name ${APPNAME}-dev-euw-webapp --resource-group $RGNAME --docker-custom-image-name robertoprevato/${APPNAME}:0.1
```

To use Basic pricing plan:
```js
    "name": "B1",
    "tier": "Basic",
    "size": "B1",
    "family": "B",
    "capacity": 1
```