#To Create a board position using numbers which look like keypad.
#7    8    9

#4    5    6

#1    2    3

Board={'7':' ','8':' ','9':' ',
       '4':' ','5':' ','6':' ',
       '1':' ','2':' ','3':' '}
board_keys=[]
for i in Board:
    board_keys.append(i)


#Creating a function for printing the board.
    
def printboard(board):
    print(board['7']+'|'+board['8']+'|'+board['9'])
    print('-+-+-')
    print(board['4']+'|'+board['5']+'|'+board['6'])
    print('-+-+-')
    print(board['1']+'|'+board['2']+'|'+board['3'])

#Creating a function to play the real game.

def game(X,Y):
    turn='X'
    count=0
    for i in range(10):
        printboard(Board)
        if turn=='X':
            print("Now It's "+ X +" turn")
        else:
            print("Now It's "+ Y +" turn")
        move=input("Enter Which Place Your "+turn+" will be located: ")
        if Board[move]==' ':
            Board[move]=turn
            count+=1
        else:
            print("This place is already filled.\nChoose other place??")
            continue
        if count>=5:
            if Board['7']==Board['8']==Board['9']!=' ':
                printboard(Board)
                print("\n Game Over.\n")
                if turn=='X':
                    print("**"+ X +"  won  ")
                else:
                    print("**"+ Y +"  won  ")
                break

            elif Board['4']==Board['5']==Board['6']!=' ':
                printboard(Board)
                print("\n Game Over.\n")
                if turn=='X':
                    print("**"+ X +"  won  ")
                else:
                    print("**"+ Y +"  won  ")
                break

            elif Board['1']==Board['2']==Board['3']!=' ':
                printboard(Board)
                print("\n Game Over.\n")
                print("**"+turn+"won.**")
                break

            elif Board['1']==Board['4']==Board['7']!=' ':
                printboard(Board)
                print("\n Game Over.\n")
                if turn=='X':
                    print("**"+ X +"  won  ")
                else:
                    print("**"+ Y +"  won  ")
                break
            elif Board['2']==Board['5']==Board['8']!=' ':
                printboard(Board)
                print("\n Game Over.\n")
                if turn=='X':
                    print("**"+ X +"  won  ")
                else:
                    print("**"+ Y +"  won  ")
                break
            elif Board['3']==Board['6']==Board['9']!=' ':
                printboard(Board)
                print("\n Game Over.\n")
                if turn=='X':
                    print("**"+ X +"  won  ")
                else:
                    print("**"+ Y +"  won  ")
                break
            elif Board['7']==Board['5']==Board['3']!=' ':
                printboard(Board)
                print("\n Game Over.\n")
                if turn=='X':
                    print("**"+ X +"  won  ")
                else:
                    print("**"+ Y +"  won  ")
                break
            elif Board['1']==Board['5']==Board['9']!=' ':
                printboard(Board)
                print("\n Game Over.\n")
                if turn=='X':
                    print("**"+ X +"  won  ")
                else:
                    print("**"+ Y +"  won  ")
                break
            
        if count==9:
            print("Game Over.\n")
            print("It's a Tie!!")
            
        if turn=='X':
            turn='O'
        else:
            turn='X'
            
    restart=input("Do You Want TO Play Again?? (Y/N)")
    if restart=='y' or restart=='Y':
        for i in board_keys:
            Board[i]=" "
        game()


if __name__=="__main__":
    print("<><><><><>  TIC  TAC  TOE  <><><><><>")
    player1=input("Enter Player1 Name: ")
    player2=input("Enter Player2 Name: ")
    game(player1,player2)

