#coding:utf-8
import datetime
import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')

db = client.papers

collection = db.books

book = {"author": "Mike",
 "text": "My first book!",
 "tags": ["爬虫", "python", "网络"],
"date": datetime.datetime.utcnow()
 }
book_id= collection .insert(book)

books = [{"author": "Mike",
 "text": "My first book!",
 "tags": ["爬虫", "python", "网络"],
"date": datetime.datetime.utcnow()
 },{"author": "qiye",
 "text": "My sec book!",
 "tags": ["hack", "python", "渗透"],
"date": datetime.datetime.utcnow()
 }]
books_id = collection.insert(books)


collection.find_one({"author": "qiye"})
for book in collection.find():
    print book
for book in collection.find({"author": "qiye"}):
    print book

collection.find({"author": "qiye"}).count()

collection.update({"author": "qiye"},{"$set":{"text":"python book"}})

collection.remove({"author": "qiye"})

