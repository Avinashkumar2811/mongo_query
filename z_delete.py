#To delete any particular documents

#DELETE - ( {"filter_conditions"} )

db.students.deleteOne( {"name":"pintu"} )
# { acknowledged: true, deletedCount: 1 }


db.students.deleteMany( {"name":"raja"} )
# { acknowledged: true, deletedCount: 2 }



# DELETE QUERIES
# 18. Delete one
db.students.deleteOne({ name: "Satyam" })

# 19. Delete many
db.students.deleteMany({ city: "Patna" })