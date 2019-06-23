

clients = 'Tomas, Juan, '

def create_client(client_name):
   global clients

   if client_name not in clients:
       clients += client_name
       _add_comma()
   else:
       print('Client is alredy in client\'s list')

def list_clients():
   print(client)

#def update_clients():


def _add_comma():
    global clients

    clients += ', '

#def _get_client_name():


def _print_line():
   print('*' * 40)


def _print_welcome():
   _print_line()
   print('WELCOME TO PLATZY VENTAS')
   _print_line()
   print('What would you like today?: ')
   print('[C]reate a client')
   print('[L]ist clients')

def _show_clients_and_execute_command(command):
   print('Current clients:')
   print('')
   list_clients()
   _print_line()

    command()

   print('')
   _print_line()
   print('Updated clients:')
   list_clients()


if __name__ == '__main__':
   _print_welcome()
   command = input()


    
