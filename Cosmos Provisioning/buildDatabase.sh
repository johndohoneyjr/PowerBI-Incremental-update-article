#! /bin/bash

# Create a Cosmos SQL API database and container with autoscale

# Variable block
let "randomIdentifier=$RANDOM*$RANDOM"
location="East US"
resourceGroup="msdocs-cosmosdb-rg-$randomIdentifier"
tag="autoscale-sql-cosmosdb"
account="cosmos-account-$randomIdentifier" #needs to be lower case
database="TestPBIX"
container="Blogger"
partitionKey="/country"
maxThroughput=1000 

az login

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