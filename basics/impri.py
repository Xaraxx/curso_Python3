
def run():
   with open('numeros.txt','w') as f:
       for i in range(10):
           f.write(str(i))

# without the context manager with! we have to include this peace of code 
#   try:
#       f = open() 
#   finally:
#       f.close()

if __name__ == '__main__':
    run()
