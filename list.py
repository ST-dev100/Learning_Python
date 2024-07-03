lis = ["hey","you"]
lis.append('ducati')
lis.insert(0, 'barak')
print(lis)
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop() 
print(motorcycles)
print(popped_motorcycle)
too_expensive = 'honda'
motorcycles.remove(too_expensive)
print(motorcycles)


#Sorting a List Permanently with the sort() Method

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

#Sorting a List Temporarily with the sorted() Function
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

#Printing a List in Reverse Order

print(cars)
cars.reverse()
print(cars)

#Finding the Length of a List
cars = ['bmw', 'audi', 'toyota', 'subaru']
len(cars)

#Looping Through an Entire List

magicians = ['alice', 'david', 'carolina'] 
for magician in magicians: 
   print(f"{magician.title()}")
print("My name is sima")

#Making Numerical Lists Using the range() Function

for value in range(1, 5):
 print(value)
print("'''''''''")
for value in range(5):
 print(value)
print("'''''''''")
for value in range(0,6,2):
 print(value)
print("'''''''''")
sqaures = []
for num in range(6):
  sqaures.append(num ** 2)
print(sqaures)  

#Simple Statistics with a List of Numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print("'''''''''")
print(max(digits))
print("'''''''''")
print(sum(digits))

#List Comprehensions

sqaures = [value ** 2 for value in range(1,11)]

print("'''''''''")\

print(sqaures)

#Slicing a List
players = ['charles', 'martina', 'michael', 'florence', 'eli'] 
print(players[0:3])
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:])
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])

#Copying a List

my_foods = ['pizza', 'falafel', 'carrot cake']

freind_food = my_foods[:]

freind_food.pop()

print("My foods")
print(my_foods)
print("Freinds foods")
print(freind_food)
