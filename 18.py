import json

x = {
  "name": "ANUJ",
  "age": 24,
  "city": "Pokhara"
}

y = json.dumps(x)
jsonDict = json.loads(y)

print ("your name:", jsonDict['name'])
print ("your age:", jsonDict['age'])


#print(json.loads(jsonDict))