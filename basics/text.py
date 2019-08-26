def run():
   counter = 0
   with open('LHC.txt','r') as f:
#       print(f.readlines())
       for line in f:
           counter += line.count('the')

   print('experiment se encuentra {} en el texto'.format(counter))

if __name__ == '__main__':
   run()
   
