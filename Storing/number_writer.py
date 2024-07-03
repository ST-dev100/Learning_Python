import json

lis = [56,96,80,33]

with open("numbers.json",'w') as f:
    json.dump(lis,f)