## How to deploy using Azure CLI

Create variables, to avoid repetition. Use an unique name for APPNAME.
```bash
export APPNAME=exampleaspnetcore
export RGNAME=${APPNAME}-dev-euw-rg
```

Create resource group.
```bash
az group create --name $RGNAME --location "westeurope"
```

Change the parameters file, to specify `dockerImageName` and an unique application name:
```js
{
  "$schema": "https://schema.management.azure.com/schemas/2015-01-01/deploymentParameters.json#",
  "contentVersion": "1.0.0.0",
  "parameters": {
    "applicationName": {
      "value": ""
    },
    "dockerImageName": {
      "value": "<TODO>"
    }
  }
}
```

Deploy application inside this resource group.
```bash
az group deployment create --name example --resource-group $RGNAME --template-file azuredeploy.json --parameters azuredeploy.parameters.json
```

Given ARM template works with a public container registered in Docker Hub, providing the `dockerImageName` parameter.