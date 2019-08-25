import math

# It is deprecated 
greet_old = 'Hello %s!'
greet_old % 'Fabrizio'

greet_positional = 'Hello {} {}!'
greet_positional.format('Fabrizio','Romano') 

greet_positional_idx = 'This is {0}! {1} loves {0}!'
greet_positional_idx.format('Python','Fabrizio')

keyword = 'Hello, my name is {name} {last_name}'
keyword.format(name = 'Fabrizio', last_name = 'Romano')

name = 'Fab'
age = 42
f"Hello! my name is {name} and I'm {age}"
f"No arguin with {math.pi}, it's irrational..."

# Checkout the offitial documentation!!
# The last one is pretty cool! ;)

t = ()


