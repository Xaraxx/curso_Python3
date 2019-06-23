clients = 'pablo, ricardo, '

def create_client(client_name):
   global clients

   if client_name not in clients:
       clients += client_name
       _add_comma()
   else:
       print('Client alredy is in the client\'s list'
 )

def list_clients():
   global clients
   print(clients)

def _get_not_client_list():
   return print('Client name is not in clients list')


def update_client(client_name, updated_client_name):
   global clients

   if client_name in clients:
       clients = clients.replace(client_name + ',', updated_client_name + ',')
   else:
       client_name = _get_not_client_list()

def delete_client(client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',', '' )
    else:
        client_name = _get_not_client_list()

def search_client(client_name):
   clients_list = clients.split(',')

   for client in clients_list:
       if client != client_name:
           continue
       else:
           return True


def _add_comma():
   global clients
   clients += ','

def _print_welcome(): 
   print('*'*40)
   print('WELCOME TO PLATZI VENTAS ')
   print('*'*40)
   print('What do you like to do today?')
   print('[C]reate client')
   print('[U]pdate client')
   print('[D]elete client')
   print('[S]earch client')
   
def _get_client_name():
    return input('What is the client name?')

if __name__ == '__main__':
   _print_welcome()
   
   command = input()
   command = command.upper()
   
   if command == 'C':
       client_name = _get_client_name()
#       client_name = input('What is the client name?')
       create_client(client_name)
       list_clients()
   elif command == 'D':
       list_clients()
       client_name = _get_client_name()
       delete_client(client_name)
       list_clients()
   elif command == 'U':
       list_clients()
       client_name = _get_client_name()
       updated_client_name = input('What is the updated client name?')
       update_client(client_name, updated_client_name)
       list_clients()
   elif command == 'S':
       client_name = _get_client_name()
       found = search_client(client_name)
       if found: 
           print('The client is in the client list')
       else:
           print('The client: {}  isn\'t in the client\'s list'.format(client_name))
   else:
       print('Invalid command')

