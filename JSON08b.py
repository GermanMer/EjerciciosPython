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

import json

InvalidJsonData = """{ "company":{ "employee":{ "name":"emma", "payble":{ "salary":7000 "bonus":800} } } }"""

json.loads(InvalidJsonData)
#json.decoder.JSONDecodeError: Expecting ',' delimiter: line 1 column 68 (char 67)
