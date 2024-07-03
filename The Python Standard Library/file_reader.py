# with open('pi_digits.txt') as file_object:
#  contents = file_object.read()
# print(contents)
# import os

# current_directory = os.getcwd()
# print(current_directory)
import os

current_directory = os.getcwd()
# file_path = os.path.join(current_directory,"The Python Standard Library", "pi_digits.txt")

with open("The Python Standard Library/pi_digits.txt") as file_object:
    content = file_object.read()
    print(content)
# print(file_path)

"""Reading Line by Line"""

with open("The Python Standard Library/pi_digits.txt") as file_object:
  for line in file_object:
    print(line.rstrip())

with open("The Python Standard Library/pi_digits.txt") as file_object:
  lines = file_object.readlines()
for line in lines:
 print(line.rstrip())  
 print(lines)