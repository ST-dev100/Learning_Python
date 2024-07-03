cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())    

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
 print("Hold the anchovies!")

 age = 21
 age2 = 18
 if (age > 10) and (age2 > 10):
    print("Adult")        

 #Checking Whether a Value Is in a List

 requested_toppings = ['mushrooms', 'onions', 'pineapple']

 if 'mushrooms' in requested_toppings:
    print("it's been in the list")   

 #Checking Whether a Value Is Not in a List
 
banned_users = ['andrew', 'carolina', 'david']

user = "maria"

if user not in banned_users:
   banned_users.append(user)
print(banned_users)

#Boolean Expressions

game_Active = True

age = 12
if age < 4:
 print("Your admission cost is $0.")
elif age < 18:
 print("Your admission cost is $25.")
else:
 print("Your admission cost is $40.")

 #testing Multiple Conditions

requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
 print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
 print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
 print("Adding extra cheese.")
print("\nFinished making your pizza!")