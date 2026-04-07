from pymongo import MongoClient

#Create connection
client = MongoClient("mongodb://localhost:27017/")

#Database
db= client["invoice_ai_app"]

#Collection

invoice_collection = db["invoices"]