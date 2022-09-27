import asyncio
from azure.cosmos.aio import CosmosClient
import os
import json
import uuid

# ----------------------------------------------------------------------------------------------------------
# Prerequistes -
#
# 1. An Azure Cosmos account -
#    https://docs.microsoft.com/azure/cosmos-db/create-cosmosdb-resources-portal#create-an-azure-cosmos-db-account
#
# 2. Microsoft Azure Cosmos PyPi package -
#    https://pypi.python.org/pypi/azure-cosmos/
#
# 3. Async http client/server framework
#    https://pypi.org/project/aiohttp/
# ----------------------------------------------------------------------------------------------------------
SAMPLE_DATA='out.json'
HOST = '<Cosmos DB URI>'
MASTER_KEY = '<Cosmos Primary Key here>'
#DONT Change these, at least the first time around
#Keeping these names, below, limits the changes in the PBIX File to Just the HOST name above
DATABASE_ID = 'TestPBIX'
CONTAINER_ID = 'Blogger'

async def create_items(container):

    path = os.path.realpath(__file__)
    dir = os.path.dirname(path)
    dir = dir.replace('cosmos-loader', 'data')
    os.chdir(dir)

    print('\nCreating Items\n')
    with open(SAMPLE_DATA, "r") as load_data:
      LOAD_DATA = json.load(load_data);

    for doc in LOAD_DATA:
      doc['id'] = str(uuid.uuid4())
      await container.create_item(body=doc)

    print('\nData load complete\n')

async def load_data():
    async with CosmosClient(HOST, {'masterKey': MASTER_KEY}, user_agent="CosmosDBPythonQuickstart", user_agent_overwrite=True) as client:

      db = client.get_database_client(DATABASE_ID)
      print('Database with id \'{0}\' was found'.format(DATABASE_ID))

      container = db.get_container_client(CONTAINER_ID)
      print('Container with id \'{0}\' was found'.format(CONTAINER_ID))

      await create_items(container)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(load_data())
