from create.py import db

#READ USING FILTER CONDITIONS 

#to get a document - ( {"key":"value"})
db.students.find( {"name":"raja"} )     #findMany nhi hota , find() hota hai - gives all documents
# db.students.find( {"name":"raja"} )
# [
#   { _id: ObjectId('692aab7d049377364535087c'), name: 'raja', age: 24 },
#   { _id: ObjectId('692ab6b7aa111c2fa0cdcdf6'), name: 'raja', age: 32 }
# ]


db.students.findOne({"name":"raja"}) #or find_one for vs code - gives only one and pehla document
# db.students.findOne( {"name":"raja"} )
# { _id: ObjectId('692aab7d049377364535087c'), name: 'raja', age: 24 }











# 📌 FIND (READ) QUERIES
# 6. Find all documents
db.students.find()

# 7. Find first matched document
db.students.findOne( {name: "Raja"} )

# 8. Projection (only specific fields)
db.students.find(   {}, {name:1, _id:0}   )

# 9. Filter: age > 25
db.students.find(   {age: {$gt:25} }    )

# 10. Filter with AND
db.students.find(   { age: {$gt:20}, city:"Patna"  })

# 11. Filter with OR
db.students.find({
  $or: [ {age: {$gt:25} }, { city: "Patna" } ]
})

# 12. Sort ascending
db.students.find().sort({ age: 1 })

# 13. Sort descending
db.students.find().sort({ age: -1 })

# 14. Limit results
db.students.find().limit(5)

# 15. Skip for pagination
db.students.find().skip(10).limit(5)

