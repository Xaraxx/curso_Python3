
#class (object):
#    """docstring forAsterix."""
#    def __init__(self, arg):
#        superAsterix, self).__init__()
#        self.arg = arg

class Asterix:
    _ASTERIX = ['''
            `-.                        _;       | _.
   `-._     `-.                   .'/ _.sssP^"'
       `-.     `.              _./  .dP'     |
          `.     \            / :  d'        |
       .-   \     ;          : /  d'     _.sd$bs.
   `- :      ;    |     _.._ |    $    .d*'  |   `.
       `-._  |    ;.-*"'  .s$s.   $   d'     ;
       .         /       d$$$$$b  T  d'   _ /
   `_ :       ../     .-d$$$$$$P  ` .   .s$b
      _`-._  /  \   .' s$$P'          .s$$$$b
    .'      : () ;.'  .$P'   _      ,'  `"T$$   .-*'"`.
   /     .'/ \  //.   :$    / \    / _     T$ .'       \
       .' /   `'/ `.  $P   :   ;  :.' \     T'          ;
   _.-'  :     /    \ :    |db |  |db  ;  .'            |
         |    :    . .     |O$ |  |O$  |.'              |
         |    |    :-.`_   :TP |  :TP .'                |
         :    |     \       \  |   \.'                  |
         `.  |__ `._`._    _L_;   /                    ;
  [bug]   :-'  `.  `     '   `.                      /
       .'       \  \          :                   .'
      /  .d^'`.  `._.  +"`   / `-.             .-'
     :  dP'\   `      ( `-.-'     `-._______.-'  `.
     :  Tb  `._.          /            /\          \
      \  `.      ;      .'            /  \          ;
       `.       /|    .'             /    \         |
         `-._.-' |   /             .'      \        ;
                 :  :             /         ;      /
                  \ |           .'          |     :
                   `|          /            :     |
                    :    /   .'              \    ;
                     \  :   /                 ;  /
                      `.| .'`.              .'| /
                        |/    `-.__    __.-'  ;/
                                   `""'
    ''',

    '''                                 _
                              _(_)
                          .-*"    `.
                          L_____   ."T  _
                          :\  `,`:.`"\.' ;
                          |_, _: : `.,+._:
                         /;s; s'  \  ;P;_.
                        .+*'  `_   `.J-  :
                       :   *'._,*,  (J)-.*
                       :      /""*+' (L)
                  s..s()l-._.'--*"    `()  _
            ___   _T$$o ;             T$bs$P-._
  .-*'"*+.*"   "*"  d$b `          /   T$*Tb   `--*""*.
 /        \        sP Ts `-.____.-'    dP  `*          `.
(`         ,      /        .'                     _    `.\
 \         :    _:       .'                     .'       `)
  \         L_.' ;___   /                      /         /
   `-.    .' ._.'_   ""**--..__         _    //         /
      `"*/    /   \.*""*.  .-._""**--._: \.-'/         /
        (((( :",  / .-. ;'  _ ""**--.._\ `-+        ,'
        :.;: :"  :  *-' /  : ;          `:   `   _.-'
         \:; ;._.'`._.-'`,  "           .',    :')
         /;: ;     ;      `""**--..___ / /; ,,,::
        : `'T                   /    \T /-;.',.':
            ;     :            :      \"   "*T"*(
       :          ;            ;       ;      \  ;
       :   :      :                    :       ; :
       ;   ;                  :                : :
       :   :       ;          ;         ;      : :
                   :          :         :      ; ;
        \   \       \                   ;
         `.  `.      \         ;              : /
           `.  `.     `.       :     .'/.    /.'
             `*-.`-.__  `-.     \   /.'\  ,.+'
                 "*-._:-'  J__..-+-*"\  ; :
                      ; -*'/          ; : ;
                      :   :   [bug]   : ;
                       \   `.         : |:
                      .-`.__J.      .-; |;._ _.-**-.
                   .--`-.___.-'-.  :.'`"'\_.' __..-*;
               .*"( ___         : : `"""*-'.-'__...-'
               ; .'`-._"*-._.--*' `"*----**""'
               `***---+***'
                                           .'    .$$$^*       _..._
                                         .'     .^^' '''
    ]

   def __init__(self, is_asterix):
       self._is_asterix = is_asterix

   def who_is(self):
       self._is_asterix = True
       self._display_image()

   def whois(self):
       self._is_asterix = False
       self._display_image()

   def _display_image(self):
       if self._is_asterix:
           print(self._ASTERIX[0])
       else:
           print(self._ASTERIX[1])

def run():
   asterix = Asterix(is_asterix=False)

   while True:
       command = str(raw_input('''
       Cual personaje es tu preferido?
       [A]sterix
       [O]belix
       [S]alir
       '''))
       if command == 'A':
           asterix.who_is()
       elif command == 'O':
           asterix.whois()
       else:
           break


if __name__ == '__main__':
   run()
