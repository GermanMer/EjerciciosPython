#Exercise 3: PrettyPrint following JSON data
#PrettyPrint following JSON data with indent level 2 and key-value separators should be (",", " = ").

#sampleJson = {"key1": "value1", "key2": "value2", "key3": "value3"}
#Expected Output:
#{
#  "key1" = "value1",
#  "key2" = "value2",
#  "key3" = "value3"
#}

import json

sampleJson = {"key1": "value1", "key2": "value2", "key3": "value3"}

json_pretty = json.dumps(sampleJson, indent=2, sort_keys=True, separators=(",", " = "))

print(json_pretty)
