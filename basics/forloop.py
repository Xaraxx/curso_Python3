
#for i in range(5):
#   print(i)

# No entiendo este código, el resultado debería ser todos los números entre 1 y 30 que al ser divididos entre 3 el residuo sea igual a cero, y esa no es la salida que se obtiene. 
# ya entendí el código funciona así: si al tomar el número y dividirlo entre 3 el residuo es igual a cero; es decir la división es exacta, el iterador pasa el número y continúa con la iteración, mientras que si es distinto de cero lo imprime!!

#for i in range(31):
#   if i % 3 == 0:
#       continue
#   else:
#       print(i)

#for i in range(101):
#   if i % 2 == 0:
#       print(i)
#   elif i == 50:
#       break

word = 'almacenaje'

for letter in word:
   if letter == 'a':
       print(letter)
   else:
       continue
