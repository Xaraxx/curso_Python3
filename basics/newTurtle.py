import turtle

def main():
   window = turtle.Screen()
   dave = turtle.Turtle()
    
   make_square(dave)
   make_square2(dave)
   turtle.mainloop()

def make_square(dave):
   length = int(input('Tamaño de cuadrado: '))
   
   for i in range(4):
       make_line_and_turn(dave, length)

def make_line_and_turn(dave,length):
   dave.forward(length)
   dave.left(90)

def make_square2(dave):
   length = int(input('Tamaño de cuadrado: '))

   for i in range(4):
       make_line_and_turn(dave, length)



if __name__ == '__main__':
   main()
