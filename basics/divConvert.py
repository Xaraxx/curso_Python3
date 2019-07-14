def foreign_exchange_calculator(ammount):
   mex_to_col_rate = 145.97 

   return mex_to_col_rate * ammount


def run():
   print('**CA L C U L A D O R A  D E  D I V I S A S**')
   print('Convierte peso mexicanos a pesos colombianos.')
   print('')

   ammount = float(input('Ingresa la cantidad en pesos mexicanos = '))

   result = foreign_exchange_calculator(ammount)
   
   print('${} pesos mexicanos son ${} pesos colombianos'.format(ammount,result))


if __name__ == '__main__':
    run()

