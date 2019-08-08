
def farenheit(tempCelsius):
   tempFarenheit = (9/5)*tempCelsius + 32.0

   return tempFarenheit

def run():
   print('Temperature Converter')
   print('Convierte la temperatura de grados celsius a farenheit')
   print('')

   tempCelsius =  float(input('Ingrese una tempertura en grados celsius: '))
   result = farenheit(tempCelsius)

   print('La temperatura en grados Fareheit es: {}'.format(result))

if __name__ == '__main__':
   run()
