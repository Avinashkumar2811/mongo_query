from create.py import db

#PROJECTION means sirf whi dikhana jo chahiye name:1, age:1 etc
# ( {}, {"conditions"} )

 db.students.find( {}, {"name":1, "_id":0} )
# [
#   { name: 'Avinash' },
#   { name: 'satyam' },
#   { name: 'a' },
#   { name: 'b' }
# ]

# { "data" :{$conditions} }
 db.students.find( {"age":{$gt:18} })
# [
#   {
#     _id: ObjectId('692aaf949e0a49c8a60dad8f'),
#     name: 'satyam',
#     age: 25
#   }
# ]