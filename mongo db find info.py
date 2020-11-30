from pymongo import MongoClient

conn = MongoClient()
db = conn.news
collection = db.yahoo
rows = collection.find({})

for row in rows:
    print(row)
    print()