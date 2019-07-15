def average_temps(temps):
   sum_of_temps = 0 

   for temp in temps:
       sum_of_temps += temp
   return sum_of_temps/len(temps)

if __name__ == '__main__':
   temps = [21,23,45,67,89,6,78]

   average =  average_temps(temps)

   print('La temperatura promedio es: {}'.format(average))
