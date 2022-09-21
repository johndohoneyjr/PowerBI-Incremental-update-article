#! /bin/bash

export randomIdentifier="552189312"
resourceGroup="msdocs-cosmosdb-rg-$randomIdentifier"

az group delete --name $resourceGroup
