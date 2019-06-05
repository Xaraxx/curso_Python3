clients = 'maria, pablo, '


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


if __name__ == '__main__':
#    clients += 'david'
   list_clients()

#  create_client('david')
   create_client(str())   
   
   list_clients()
