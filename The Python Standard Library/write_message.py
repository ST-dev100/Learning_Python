filename = 'programming.txt'

with open(filename, 'w') as file_object:
  file_object.write("I love programming.")

# in read mode ('r'), write mode ('w'), append mode ('a'), or a mode that allows 
# you to read and write to the file ('r+'). If you omit the mode argument, 
# Python opens the file in read-only mode by default.  

# Writing Multiple Lines

filename = 'programming2.txt'
with open(filename, 'w') as file_object:
 file_object.write("I love programming.\n")
 file_object.write("I love creating new games.")

#  Appending to a File

filename = 'programming.txt'

with open(filename, 'a') as file_object:
 file_object.write("\nI also love finding meaning in large datasets.\n")
 file_object.write("I love creating apps that can run in a browser.\n")