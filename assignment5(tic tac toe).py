
def show():
     for row in game_board :
      for cell in row:
        print(cell, end="")
      print ()   
def check_win_player1():
     
      if game_board[0][0]=="x" and game_board[0][1]=="x" and game_board[0][2]=="x":
          print("player1 wins")
         
      if game_board[1][0]=="x" and game_board[1][1]=="x" and game_board[1][2]=="x":
          print("player1 wins")
      
      if game_board[2][0]=="x" and game_board[2][1]=="x" and game_board[2][2]=="x":
          print("player1 wins")
      if game_board[0][0]=="x" and game_board[1][0]=="x" and game_board[2][0]=="x":
          print("player1 wins")
      if game_board[0][1]=="x" and game_board[1][1]=="x" and game_board[2][1]=="x":
           print("player1 wins")
      if game_board[0][0]=="x" and game_board[1][1]=="x" and game_board[2][2]=="x":
           print("player1 wins")
           return 1
      if  game_board[0][2]=="x" and game_board[1][1]=="x" and game_board[2][0]=="x":
           print("player1 wins")

          
def check_win_player2():
     
      if game_board[0][0]=="O" and game_board[0][1]=="O" and game_board[0][2]=="O":
          print("player2 wins")
          
      if game_board[1][0]=="O" and game_board[1][1]=="O" and game_board[1][2]=="O":
          print("player2 wins")
      if game_board[2][0]=="O" and game_board[2][1]=="O" and game_board[2][2]=="O":
          print("player2 wins")
      if game_board[0][0]=="O" and game_board[1][0]=="O" and game_board[2][0]=="O":
          print("player2 wins")
        
      if game_board[0][1]=="O" and game_board[1][1]=="O" and game_board[2][1]=="O":
           print("player2 wins")
      if game_board[0][0]=="O" and game_board[1][1]=="O" and game_board[2][2]=="O":
           print("player2 wins")
      if  game_board[0][2]=="O" and game_board[1][1]=="O" and game_board[2][0]=="O":
           print("player2 wins")  
               
game_board=[["-","-","-"],
            ["-","-","-"],
            ["-","-","-"]]

show()

while True:
  print("player1")
 
  while True:
    row=int(input("enter row:"))
    col=int(input("enter col:"))
    if 0<=row<=2 and 0<=col<=2 :
#  check if it is empty then insert a charecter
      if game_board[row][col]=="-":
         game_board[row][col]="x"
         break
      else:
       print("select another cell")   
    else:
      print("select in 0,2")
  show()
  check_win_player1()


    
# ////////////////////////////////
    
  print("player2")
  if check_win_player1()!=1 and check_win_player2!=1:
      while True:
              row=int(input("enter row:"))
              col=int(input("enter col:"))
              if 0<=row<=2 and 0<=col<=2 :
      #  check if it is empty then insert a charecter
                if game_board[row][col]=="-":
                  game_board[row][col]="O"
                  break
                else:
                  print("select another cell")   
              else:
                print("select in 0,2")

      show()
      check_win_player2()
    