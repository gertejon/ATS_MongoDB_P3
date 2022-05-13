import json
from pymongo import MongoClient
cli = MongoClient('localhost', 27017)
db = cli['test']
coll = db['companies']

with open('companies/companies.json', encoding="utf8") as f:
    file_data = json.load(f)

coll.insert_many(file_data)

cli.close()