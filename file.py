import re

def generateBoard(n):
    return [1]*n

def solve(board):
    if checkBoard(board):
        return True
    elif checkUnsolvable(board):
        return False

    moves = []
    for i in range(len(board)):
        if i < len(board)-2:
            if board[i] and board[i+1] and not board[i+2]:
                moves.append((i, 'right'))
        if i > 1:
            if board[i] and board[i-1] and not board[i-2]:
                moves.append((i, 'left'))
    
    for move in moves:
        newBoard = makeMove(board, move)
        if solve(newBoard):
            return True
        continue

    return False


def makeMove(board, move):
    index, direction = move
    b = [element for element in board]
    if direction == 'right':
        b[index] = 0
        b[index+1] = 0
        b[index+2] = 1
    elif direction == 'left':
        b[index] = 0
        b[index-1] = 0
        b[index-2] = 1
    return b

def checkBoard(board):
    if sum(board) == 1:
        return True
    return False

def checkUnsolvable(board):
    expression1 = '1000+1' #RE for a proven to be unsolvable board
    expression2 = '00100'  #RE for a proven to be unsolvable board
    string = ''.join([str(element) for element in board])
    if re.search(expression1, string) or re.search(expression2, string):
        return True
    return False

def countSolutions(board):
    indices = []
    for i in range(len(board)):
        b = [element for element in board]
        b[i] = 0
        if solve(b):
            indices.append(i+1)
    return indices


n = int(input())
print(countSolutions(generateBoard(n)))