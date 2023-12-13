#Exercise 8: Check whether following json is valid or invalid. If Invalid correct it

#{
#   "company":{
#      "employee":{
#         "name":"emma",
#         "payble":{
#            "salary":7000
#            "bonus":800
#         }
#      }
#   }
#}

#Python provides the json.tool module to validate JSON objects from the command line.
#Run the following command on DOS: echo "JSON DATA" | python -m json.tool

echo {"company":{"employee":{"name":"emma","payble":{"salary":7000"bonus":800}}}} | python -m json.tool
#Expecting ',' delimiter: line 1 column 62 (char 61)

echo {"company":{"employee":{"name":"emma","payble":{"salary":7000,"bonus":800}}}} | python -m json.tool
