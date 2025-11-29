from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["mydb"]
# collection = db["students"]
# collection.insert_one({"name": "Avinash", "city": "Patna"})

#DB.COLLECTION_NAME.operations( {}, {} )


#for _one --> we use ( {} )
db.students.insert_one({"name":"raja","age":24})
#db.students.insertOne({"name":"raja","age":32})


#for _many --> we use array of documents, ( [{},{}] )
db.students.insert_many(    [ {"name":"satyam","age":25},
                        {"name":"pintu","age":30} ]   )








# 📌 INSERT QUERIES
# 4. Insert one document
# js
# Copy code
db.students.insertOne(  { name:"Avinash", age:24 }   )

# 5. Insert many documents
# js
# Copy code
db.students.insertMany(     [
  { name: "Raja", age: 30 },
  { name: "Satyam", age: 26 }
]   )
