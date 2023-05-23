from pyfiglet import Figlet
from termcolor import colored
f=Figlet(font='banner3-D')
print(colored(f.renderText('TIC  TAC  TOE'),'light_yellow'))
                            
def show():
     
     

     for row in game_board :
      for cell in row:
        print(cell, end="")
      print ()   

def show_winner1():
    from pyfiglet import Figlet
    from termcolor import colored
    f=Figlet(font='slant')
    print(colored(f.renderText('congratulation player1 ... you win !!'),'light_red'))
    return False
def show_winner2():
    from pyfiglet import Figlet
    from termcolor import colored
    f=Figlet(font='slant')
    print(colored(f.renderText('congratulation player1 ... you win !!'),'light_red')) 

def check_win_player1():
     
      if game_board[0][0]=="x" and game_board[0][1]=="x" and game_board[0][2]=="x":
          show_winner1()
         
      if game_board[1][0]=="x" and game_board[1][1]=="x" and game_board[1][2]=="x":
          show_winner1()
      
      if game_board[2][0]=="x" and game_board[2][1]=="x" and game_board[2][2]=="x":
         show_winner1()

      if game_board[0][0]=="x" and game_board[1][0]=="x" and game_board[2][0]=="x":
        show_winner1()

      if game_board[0][1]=="x" and game_board[1][1]=="x" and game_board[2][1]=="x":
           show_winner1()

      if game_board[0][0]=="x" and game_board[1][1]=="x" and game_board[2][2]=="x":
           show_winner1()

      if  game_board[0][2]=="x" and game_board[1][1]=="x" and game_board[2][0]=="x":
           show_winner1()

          
def check_win_player2():
     
      if game_board[0][0]=="O" and game_board[0][1]=="O" and game_board[0][2]=="O":
          show_winner2()
          
      if game_board[1][0]=="O" and game_board[1][1]=="O" and game_board[1][2]=="O":
           show_winner2()
      if game_board[2][0]=="O" and game_board[2][1]=="O" and game_board[2][2]=="O":
            show_winner2()
      if game_board[0][0]=="O" and game_board[1][0]=="O" and game_board[2][0]=="O":
           show_winner2()
        
      if game_board[0][1]=="O" and game_board[1][1]=="O" and game_board[2][1]=="O":
             show_winner2()
      if game_board[0][0]=="O" and game_board[1][1]=="O" and game_board[2][2]=="O":
             show_winner2()
      if  game_board[0][2]=="O" and game_board[1][1]=="O" and game_board[2][0]=="O":
             show_winner2()
               
game_board=[["-","-","-"],
            ["-","-","-"],
            ["-","-","-"]]

show()

while True:
  
  print('player1 it is your turn . move')

 
  while True:
    row=int(input("enter row:"))
    col=int(input("enter col:"))
    if 0<=row<=2 and 0<=col<=2 :
#  check if it is empty then insert a charecter
      if game_board[row][col]=="-":
         game_board[row][col]="x"
         break
      else:
       print("!!! select another cell")   
    else:
      print("!!!please select rows and columns in range  in 0,2")
  show()
  check_win_player1()


    
# ////////////////////////////////
    
  print("player2 it is your turn . move")
  
  while True:
              row=int(input("enter row:"))
              col=int(input("enter col:"))
              if 0<=row<=2 and 0<=col<=2 :
      #  check if it is empty then insert a charecter
                if game_board[row][col]=="-":
                  game_board[row][col]="O"
                  break
                else:
                  print("!!!! select another cell")   
              else:
                print("!!!please select rows and columns in range  in 0,2")

  show()
  check_win_player2()
    
