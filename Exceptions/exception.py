try:
 print(5/1)
except ZeroDivisionError:
 print("You can't divide by zero!")

 """Handling the FileNotFoundError Exception"""

filename = 'alice.txt'
try:
 with open(filename, encoding='utf-8') as f:
  contents = f.read()
except FileNotFoundError:
 print(f"Sorry, the file {filename} does not exist.")

# Analyzing Text

title = "Alice in Wonderland"

print( title.split() )