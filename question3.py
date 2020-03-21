#!/usr/bin/python3
'''
INTERMEDIATE
Cross Game or Tic-Tac-Toe Game
a. Desc -> Write a Program to play a Cross Game or Tic-Tac-Toe Game. Player 1 is the 
Computer and the Player 2 is the user. Player 1 take Random Cell that is the Column 
and Row.
b. I/P -> Take User Input for the Cell i.e. Col and Row to Mark the ‘X’
c. Logic -> The User or the Computer can only take the unoccupied cell. The Game is 
played till either wins or till draw...
d. O/P -> Print the Col and the Cell after every step.
e. Hint -> The Hints is provided in the Logic. Use Functions for the Logic...

'''
import random
import sys

board=[i for i in range(0,9)]
player, computer = '',''
moves=((1,7,3,9),
        (5,)
        ,(2,4,6,8))

winners=((0,1,2),
        (0,3,6),
        (0,4,8),
        (1,4,7),
        (2,4,6),
        (2,5,8),
        (3,4,5),
        (6,7,8))

tab=range(1,10)

def boardShow():
    x=1
    counter = 0
    for i in range(0,9):
        if board[i] == 'X' or board[i] == 'O' :
            print(board[i],end = ' ')
        else :
            print(" ",end = ' ')
        counter+=1
        if counter%3 ==0 :
            print("",end = '\n----------\n')
        else :
            print("| ",end='')

def select_char():
    if random.randint(0,1) == 0:
        return ('X','O')
    return ('O','X')

def can_move(brd, player, move):
    if move in tab and brd[move-1] == move-1:
        return True
    return False

def can_win(brd, player, move):
    places=[]
    x=0
    for i in brd:
        if i == player: places.append(x);
        x+=1
    win=True
    for tup in winners:
        win=True
        for ix in tup:
            if brd[ix] != player:
                win=False
                break
        if win == True:
            break
    return win

def make_move(brd, player, move, undo=False):
    if can_move(brd, player, move):
        brd[move-1] = player
        win=can_win(brd, player, move)
        if undo:
            brd[move-1] = move-1
        return (True, win)
    return (False, False)

def random_move():
    move=-1
    empty_place = []
    for i in range(1,10):
        if board[i-1] == i-1 :
            empty_place.append(i)
    if len(empty_place) > 0 :
        idx = random.randint(0,len(empty_place)-1)
        move = empty_place[idx]
        return make_move(board,computer,move)
    return (False,False)

def machineMove():
    move=-1
    for i in range(1,10):
        if make_move(board, computer, i, True)[1]:
            move=i
            break
    if move == -1:
        for i in range(1,10):
            if make_move(board, player, i, True)[1]:
                move=i
                break
    if move == -1:
        for tup in moves:
            for mv in tup:
                if move == -1 and can_move(board, computer, mv):
                    move=mv
                    break
    return make_move(board, computer, move)

def is_full():
    for i in range(0,9):
        if board[i] == i:
            return True
    return False

player, computer = select_char()
print('Player is [%s] and computer is [%s]' % (player, computer))

turn = random.randint(0,1)

if turn == 0 :
    print("Player will play first.")
else :
    print("Computer will play first.")
    boardShow()
    machineMove()
    print()

result="It's a tie !!"

while is_full():
    boardShow()
    print('Make your move  [1-9] : ', end='')
    move = int(input())
    moved, won = make_move(board, player, move)
    if not moved:
        print(' >> Invalid number ! Try again !')
        continue
    if won:
        result=' You won !!'
        break
    elif machineMove()[1]:
        result=' You lose !!'
        break;

boardShow()
print(result)