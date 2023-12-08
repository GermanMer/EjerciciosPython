#Exercise 5: Access the nested key ‘salary’ from the following JSON

#sampleJson = """{
#   "company":{
#      "employee":{
#         "name":"emma",
#         "payble":{
#            "salary":7000,
#            "bonus":800
#         }
#      }
#   }
#}"""

# write code to print the value of salary

#Expected Output:
#7000

import json

sampleJson = """{
   "company":{
      "employee":{
         "name":"emma",
         "payble":{
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

data = json.loads(sampleJson)

print(data["company"]["employee"]["payble"]["salary"])
