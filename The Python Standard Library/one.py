import random

print(random.randint(1,6))

"""returns a randomly chosen element:"""

from random import choice

players = ['charles', 'martina', 'michael', 'florence', 'eli']

first_up = choice(players)

print(first_up)