from pymongo import MongoClient
from pprint import pprint

MONGO_URL = "mongodb://mongo:27017" # name from service docker-compose.yml
client = MongoClient(MONGO_URL)
db = client.admin
dbs_list = db.command("listDatabases")
pprint(dbs_list)