#! /bin/bash

export randomIdentifier="572838462"
resourceGroup="msdocs-cosmosdb-rg-$randomIdentifier"

az group delete --name $resourceGroup
