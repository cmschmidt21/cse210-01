'''
Not your MeeMaw's Tic-Tac-Toe
Author: Caitlyn Schmidt
'''
import os


# Define functions
def draw_board(boxes):
    board = (f"|{boxes[1]}|{boxes[2]}|{boxes[3]}|\n*******\n|{boxes[4]}|{boxes[5]}|{boxes[6]}|\n*******\n|{boxes[7]}|{boxes[8]}|{boxes[9]}|")
    print(board)

def check_turn(player_turn):
    if player_turn % 2 == 0: return 'O'
    else: return 'X'

def check_win(boxes):
    #horizontal checks
    if (boxes[1] == boxes[2] == boxes[3])\
        or (boxes[4] == boxes[5] == boxes[6])\
        or (boxes[7] == boxes[8] == boxes[9]):
            return True
    #vertical checks
    if (boxes[1] == boxes[4] == boxes[7])\
        or (boxes[2] == boxes[5] == boxes[8])\
        or (boxes[3] == boxes[6] == boxes[9]):
            return True
    #diagonal checks
    elif (boxes[1] == boxes[5] == boxes[9])\
        or (boxes[3] == boxes[5] == boxes[7]):
            return True
    else: return False

def main():
    boxes = {1 : '1', 2 : '2', 3 : '3', 4 : '4', 
    5 : '5', 6 : '6', 7 : '7', 8 : '8', 9 : '9'}

    draw_board(boxes)

    game_active = True
    player_turn = 0
    previous_turn = -1
    winner = False


    while game_active:
        #Clear the screen
        os.system('cls' if os.name == 'nt' else 'clear')
        draw_board(boxes)
        # Tell the player if they entered an invalid value.
        if previous_turn == player_turn:
            print()
            print("Invalid input, please try again.")
        previous_turn = player_turn
        print()
        print("Player " + str((player_turn % 2) + 1 )+ "'s turn: Pick your spot or press q to quit the game.")
        print()
        #Ask player to make a choice
        choice = input("Where would you like to place your symbol? ")
        if choice == "q":
            game_active = False
            print()
            print()
            print("Thanks for playing! See you next time!")
            print()
            print()
        #Check for validation of input
        elif str.isdigit(choice) and int(choice) in boxes:
            if not boxes[int(choice)] in {"X", "O"}:
                #change the board if it is a valid input
                player_turn += 1
                boxes[int(choice)] = check_turn(player_turn)
        #Check to see if someone has won and the game has ended. 
        if check_win(boxes): game_active, winner = False, True
        if player_turn > 8: game_active = False

    #Print the game results
    os.system('cls' if os.name == 'nt' else 'clear')
    draw_board(boxes)

    #If there was a winner, let them know they won!
    if winner:
        if check_turn(player_turn) == "X":
            print()
            print("Player 1 Wins!")
            print()
        else:
            print()
            print("Player 2 Wins!")
            print()
    else: 
        print("There is no winner!")

    print()
    print("Thanks for Playing!!")
    print()
    



if __name__ == "__main__":
    main()
