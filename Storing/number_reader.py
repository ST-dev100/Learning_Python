import json;

with open("numbers.json",'r') as f:
   numbers = json.load(f)

print(numbers)

try:
    with open("name.json") as f:
        names = json.load(f)
except FileNotFoundError:
    name = input("enter yout name ")        
    with open("name.json",'w') as f:
        json.dump(name,f)
else:
    print(names)
        
      