from create.py import db

#UPDATE ME - ( {pehle_filter_nikalo}, {$set : {jo_chnage_krna_hai_wo_set} } )

#to update only single document
db.students.updateOne( {"name": "pintu"} , { $set: {"age":78} } )
# {
#   acknowledged: true,
#   insertedId: null,
#   matchedCount: 1,
#   modifiedCount: 1,
#   upsertedCount: 0
# }


#To update many documents in one go
db.students.updateMany( {"name": "raja"} , {$set: {"age":80} })
# {
#   acknowledged: true,
#   insertedId: null,
#   matchedCount: 2,
#   modifiedCount: 2,
#   upsertedCount: 0
# }






# UPDATE QUERIES
# 16. Update one
db.students.updateOne(
  { name: "Raja" },
  { $set: { age: 40 } }
)

# 17. Update many
db.students.updateMany(
  { city: "Patna" },
  { $set: { status: "active" } }
)