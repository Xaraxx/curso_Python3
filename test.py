clients = 'pablo, ricardo, '

def create_client(client_name):
   global clients

   clients += client_name
   _add_comma() 

def list_clients():
   global clients
   print(clients)

def _add_comma():
   global clients
   clients += ','

def _print_welcome():
   print('WELCOME TO PLATZI VENTAS ')
   print('*'*40)
   print('What do you like to do today?')
   print('[C]reate client')
   print('[D]elete client')
   
if __name__ == '__main__':
   _print_welcome()
   
   command = input()
   
   if command == 'C':
       client_name = input('What is the client name? ')
       create_client(client_name)
       list_clients()
   elif commad == 'D':
       pass
   else:
       print('Invalid command')

