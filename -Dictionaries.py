alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

#Adding New Key-Value Pairs
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#Modifying Values in a Dictionary

alien_0['color'] = 'yellow'

#Removing Key-Value Pairs

alien_0 = {'color': 'green', 'points': 5}

print(alien_0)

del alien_0['points']

print(alien_0)

#Using get() to Access Values

print(alien_0.get("point","it doesn't exist"))

#Looping Through a Dictionary

user_0 = {
 'username': 'efermi',
 'first': 'enrico',
 'last': 'fermi',
 }

for key,value in user_0.items():
    print(f"\nkey: {key}")
    print(f"value: {value}")

#Looping Through All the Keys in a Dictionary

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

for name in favorite_languages.keys():
    print(name.title())

#Looping Through a Dictionary’s Keys in a Particular Order

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
for name in sorted(favorite_languages.keys()):
 print(f"{name.title()}, thank you for taking the poll.")

#Looping Through All Values in a Dictionary 

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
print("The following languages have been mentioned:")
for language in favorite_languages.values():
 print(language.title())

#A List of Dictionaries

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
 print(alien)

#A List in a Dictionary

order = {'food_name':"doro",'ingrediant':["salt","onion","oil"]}

for key,value in order.items():
  for v in value:
    print(v)

#A Dictionary in a Dictionary
users = {
 'aeinstein': {
 'first': 'albert',
 'last': 'einstein',
 'location': 'princeton',
 },
 'mcurie': {
 'first': 'marie',
 'last': 'curie',
 'location': 'paris',
 },
 }
for key , value in users.items():
    print(f"{value['first']} - {value['last']} - {value['location']}")