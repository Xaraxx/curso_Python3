import random

# modificar este código cambiando el rango de los números aleatorios 

def run():
   number_found = False
   random_number = random.randint(0, 20) 

   while not number_found:
       number = int(input('ingresa un número entero: '))
       
       if number == random_number:
           print('Felicidades. Encontraste el número')
           number_found = True 
       elif number > random_number:
           print('El número es más pequeño')
       else:
           print('El número es más grande')

if __name__ == '__main__':
   run()
