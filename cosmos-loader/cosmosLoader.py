import json
import azure.cosmos.documents as documents
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.exceptions as exceptions
from azure.cosmos.partition_key import PartitionKey
import datetime
import uuid

# ----------------------------------------------------------------------------------------------------------
# Prerequistes -
#
# 1. An Azure Cosmos account -
#    https://docs.microsoft.com/azure/cosmos-db/create-cosmosdb-resources-portal#create-an-azure-cosmos-db-account
#
# 2. Microsoft Azure Cosmos PyPi package -
#    https://pypi.python.org/pypi/azure-cosmos/
# ----------------------------------------------------------------------------------------------------------
SAMPLE_DATA="C:\\Users\\<Your User Name>\\PowerBI-Incremental-update-article\\data\\out.json"
HOST = 'https://cosmos-account-552189312.documents.azure.com:443/'
MASTER_KEY = '<Cosmos Primary Key here>'
#DONT Change these, at least the first time around
#Keeping these names, below, limits the changes in the PBIX File to Just the HOST name above
DATABASE_ID = 'TestPBIX'
CONTAINER_ID = 'Blogger'

def create_items(container):
    print('\nCreating Items\n')
    with open(SAMPLE_DATA, "r") as load_data:
      LOAD_DATA = json.load(load_data);

    for doc in LOAD_DATA:
      doc['id'] = str(uuid.uuid4())
      container.create_item(body=doc)

def load_data():
    client = cosmos_client.CosmosClient(HOST, {'masterKey': MASTER_KEY}, user_agent="CosmosDBPythonQuickstart", user_agent_overwrite=True)

    db = client.get_database_client(DATABASE_ID)
    print('Database with id \'{0}\' was found'.format(DATABASE_ID))

    container = db.get_container_client(CONTAINER_ID)
    print('Container with id \'{0}\' was found'.format(CONTAINER_ID))

    create_items(container)

if __name__ == '__main__':
    load_data()