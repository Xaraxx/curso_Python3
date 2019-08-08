#List Comprenhention 
# Is method for resume your code and makeit more readable 
pares = []

for i in range(1, 31):
   if i % 2 == 0.0:
       pares.append(i)
print(pares)

# List Comprenhention
# note: you have to remember this sintax

pares2 = [i for i in range(1, 31) if i % 2 == 0 ]
print(pares2)

cuadrados = {}

for i in range(1, 11):
    cuadrados[i] = i**2

print(cuadrados)

squares = {i : i**2 for i in range(1,11)}

print(squares) 

# Note search more about 'sintactic sugar' and modify past codes
