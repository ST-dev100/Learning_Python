"""
Define a function and do task

"""

def greet_user():
    print("Hello User")

greet_user()    

def greet_user(username):
 """Display a simple greeting."""
 print(f"Hello, {username.title()}!")
 
greet_user('jesse')

#Keyword Arguments
def describe_pet(animal_type, pet_name):
 """Display information about a pet."""
 print(f"\nI have a {animal_type}.")
 print(f"My {animal_type}'s name is {pet_name.title()}.")
 
describe_pet(animal_type='hamster', pet_name='harry')

#Default Values

def defaultValue(a,b="The Man!"):
  print(f"{a} {b}")

defaultValue(a="Simon")

""" Return Values """

def returnValues(a,b):
  return a+b

sum = returnValues(3,4)
print(sum)

""" Returning a Dictionary """

def build_person(first_name, last_name):
 """Return a dictionary of information about a person."""
 person = {'first': first_name, 'last': last_name}
 return person

musician = build_person('jimi', 'hendrix')
print(musician)

def build_person(first_name,last_name,age=None):
  person = {'first':first_name,'last':last_name}
  if age:
    person['age'] = age
  return person

person1 = build_person("Simon","Tamene",26);

print(person1)


""" Passing a List """

def greet_users(names):
  """Print a simple greeting to each user in the list."""
  for name in names:
     msg = f"Hello, {name.title()}!"
     print(msg)

usernames = ['hannah', 'ty', 'margot']

greet_users(usernames)

""" Passing an Arbitrary Number of Arguments """

def make_pizza(*toppings):
 """Print the list of toppings that have been requested."""
 print(type(toppings))
 
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

""" Mixing Positional and Arbitrary Arguments """

def make_pizza(size, *toppings): 
 """Summarize the pizza we are about to make."""
 print(f"\nMaking a {size}-inch pizza with the following toppings:") 
 for topping in toppings: 
   print(f"- {topping}") 
 
make_pizza(16, 'pepperoni') 
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

""" Using Arbitrary Keyword Arguments """

def build_profile(first, last, **user_info):
  user_info['first_name'] = first
  user_info['last_name'] = last
  return user_info
user_profile = build_profile('albert', 'einstein',
 location='princeton',
 field='physics')
print(user_profile)