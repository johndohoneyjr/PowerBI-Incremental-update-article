#! /bin/bash

# Create a Cosmos SQL API database and container with autoscale

# Variable block
let "randomIdentifier=$RANDOM*$RANDOM"
location="East US"
resourceGroup="pbi-incr-update-$randomIdentifier"
tag="autoscale-sql-cosmosdb"
account="pbi-cosmos-$randomIdentifier" #needs to be lower case
database="TestPBIX"
container="Blogger"
partitionKey="/country"
maxThroughput=1000 

subscriptionId='<enter your subscription id here>'

az login

#set current subscription
az account set -s $subscriptionId

# Create a resource group
echo "Creating $resourceGroup in $location..."
az group create --name $resourceGroup --location "$location" --tags $tag

# Create a Cosmos account for SQL API
echo "Creating $account"
az cosmosdb create --name $account --resource-group $resourceGroup --default-consistency-level Eventual --locations regionName="$location" failoverPriority=0 isZoneRedundant=False

# Create a SQL API database
echo "Creating $database"
az cosmosdb sql database create --account-name $account --resource-group $resourceGroup --name $database

# Create a SQL API container with autoscale
echo "Creating $container with $maxThroughput"
az cosmosdb sql container create --account-name $account --resource-group $resourceGroup --database-name $database --name $container --partition-key-path $partitionKey --max-throughput $maxThroughput

# output the uri and key for the cosmosLoader.py script
uri=$(az cosmosdb show --resource-group $resourceGroup --name $account --query documentEndpoint)
key=$(az cosmosdb keys list --resource-group $resourceGroup --name $account --type keys --query primaryMasterKey)
echo "HOST = $uri"
echo "MASTER_KEY = $key"