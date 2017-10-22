## How to deploy using Azure CLI

Create variables, to avoid repetition. Use an unique name for APPNAME.
```bash
export APPNAME=aspcorehelloworld
export RGNAME=${APPNAME}-dev-euw-rg
```

Create resource group.
```bash
az group create --name $RGNAME --location "westeurope"
```

Deploy application inside this resource group.
```bash
az group deployment create --name example --resource-group $RGNAME --template-file azuredeploy.json --parameters azuredeploy.parameters.json
```

Given ARM template already works with a public container registered in Docker Hub.