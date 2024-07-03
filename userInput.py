message = input("Tell me something, and I will repeat it back to you: ")
print(message)
age = input("How old are you? ")
age = int(age)
if (int(age)>=18):
    print("pass")
else:
    print("Fail")    

#while Loops

current_num = 0

while current_num < 5:
    print(current_num)
    current_num = current_num + 1

msg = ""

while msg != "quite":
    msg = input("Enter ")
    print(msg)

#Using break to Exit a Loop
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) " 

while True:
 city = input(prompt)
 
 if city == 'quit':
     break
 else:
     print(f"I'd love to go to {city.title()}!")

#Using continue in a Loop
current_number = 0

while current_number < 10:
 current_number += 1
 if current_number % 2 == 0:
    continue
 
 print(current_number)

 #Removing All Instances of Specific Values from a List

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
 pets.remove('cat')
 
print(pets)