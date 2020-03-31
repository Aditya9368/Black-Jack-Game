from random import randint


def display(board):
    print('\n'*100)
    print(' '+board[1]+'|'+' '+board[2]+'|'+board[3])
    print('--|--|--')
    print(' '+board[4]+'|'+' '+board[5]+'|'+board[6])
    print('--|--|--')
    print(' '+board[7]+'|'+' '+board[8]+'|'+board[9])


def player_input():
    marker = ''
    while(marker != 'X' and marker != 'O'):
        marker = input("Player 1: Choose X or O : ").upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def place_marker(board, marker, position):
    board[position] = marker


def check_win(board, mark):
    check = ((board[1] == mark and board[5] == mark and board[9] == mark) or
             (board[3] == mark and board[5] == mark and board[7] == mark) or
             (board[1] == mark and board[2] == mark and board[3] == mark) or
             (board[4] == mark and board[5] == mark and board[6] == mark) or
             (board[7] == mark and board[8] == mark and board[9] == mark) or
             (board[1] == mark and board[4] == mark and board[7] == mark) or
             (board[2] == mark and board[5] == mark and board[8] == mark) or
             (board[3] == mark and board[6] == mark and board[9] == mark))
    return check


def choose_first():
    turn = randint(0, 1)
    if turn == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board, position):
    return board[position] == ' '


def fullboard_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice():
    position = 0
    while(position not in range(1, 10) or not space_check(board, position)):
        position = int(input("Choose Position (1-9) : "))
    return position


def replay():
    choice = input("Do you want to play again ? yes or no")
    return choice == 'yes'


print("Welcome to TIC TAC TOE Game ..................")
position = 0
while True:
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    Player1marker, Player2marker = player_input()

    turn = choose_first()
    print(turn+" will play first")

    play = input("Are you ready to play ? y or n: ")
    if play == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            display(board)
            choice = player_choice()
            place_marker(board, Player1marker, choice)
            if check_win(board, Player1marker):
                display(board)
                print("Player 1 Won")
                game_on = False
            else:
                if fullboard_check(board):
                    display(board)
                    print("GAME  TIE")
                    game_on = False
                else:
                    turn = 'Player 2'
        else:
            display(board)
            choice = player_choice()
            place_marker(board, Player2marker, choice)
            if check_win(board, Player2marker):
                display(board)
                print("Player 2 Won")
                game_on = False
            else:
                if fullboard_check(board):
                    display(board)
                    print("GAME  TIE")
                    game_on = False
                else:
                    turn = 'Player 1'

    if not replay():
        break
