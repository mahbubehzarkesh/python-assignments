def draw_board(r,c):
    for row in range(r):
         board = ""
         for col in range(c):
            if r % 2 == 0:
                board += "#*"
            else:
                board += "*#"
         print(board)


n =int( input("enter number of rows:"))
m=int(input("enter number if oloumns:"))

# print("\n")
draw_board(n,m)