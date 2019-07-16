# -*- conding: utf-8 -*-
import random

IMAGES = ['''
     +----+
     |    |
          |
          |
          |
          |
          =========''', ''' 
          
     +----+
     |    |
     O    |
          |
          |
          |
          =========''','''
   
     +----+
     |    |
     O    |
     |    |
          |
          |
          ========''','''
    
     +----+
     |    |
     O    |
    /|    |
          |
          |
          =========''','''
     
     +----+
     |    |
     O    |
    /|\   |
          |
          |
          =========''','''
     
     +----+
     |    |
     O    |
    /|\   |
     |    |
          |
          =========''','''
     
     +----+
     |    |
     O    |
    /|\   |
     |    |
    /     |
          =========''','''
     
     +----+
     |    |
     O    |
    /|\   |
     |    |
    / \   |
          =========''','''
  ''']
WORDS = [
        'lavadora',
        'secadora',
        'cocina',
        'medicina',
        'hipotalamo',
        'hipnosis',
        'pareidoleo',
        'sinapsis',
        'neurosis',
        'histeria'
        'Hipatia',
        'meningitis',
        'trituradora',
        'teclado',
        'mouse'
]

def random_word():
   idx = random.randint(0, len(WORDS) - 1)
   return WORDS[idx]

def display_board(hidden_word,tries):
   print(IMAGES[tries])
   print('')
   print(hidden_word)
   print('--- * --- * --- * --- * --- * ') 
  
def run():
   word = random_word()
   hidden_word = ['-']*len(word)
   tries = 0
   
   while True:
       display_board(hidden_word,tries)
       current_letter = str(raw_input('Escoje una letra: '))
      
       letter_indexes = []

# Hasta aqui el codigo funciona bien pero falta implementar la logica final del juego, es decir cuando gana o pierde una persona.

       for idx in range(len(word)):
           if word[idx] == current_letter:
               letter_indexes.append(idx)

       if len(letter_indexes) == 0:
           tries += 1
#Estas lineas son para implementar la logica del juego cuando se gana y cuando se pierde

           if tries == 7:
               display_board(hidden_word,tries)
               print('')
               print('Perdiste, la palabra correcta era {}'.format(word))
               break
        
       else:
           for idx in letter_indexes:
               hidden_word[idx] = current_letter

           letter_indexes = []
       
       try:
           hidden_word.index('-')
       except ValueError:
           print('')
           print('Felicidades!. Ganaste. La palabra es: {}'.format(word))
           break

                         
if __name__ == '__main__':
   print('B I E N V E N I D O S  A L  A H O R C A D O')
   run()
