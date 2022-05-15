def whoWins(F,S):
    
    if F == 'R' and S == 'S':
        return 1

    elif F == 'R' and S == 'P':
        return 2

    elif F == 'P' and S == 'R':
        return 1

    elif F == 'P' and S == 'S':
        return 2

    elif F == 'S' and S == 'P':
        return 1

    elif F == 'S' and S == 'R':
        return 2
    else:
        return -1


    




def rockPaperScissors(A, B, K):

    player1 = 0 # no of wins for first player
    player2 = 0 # no of wins for secnod player
    for i in range(K):
        result= whoWins(A[i%len(A)], B[i%len(B)]) 
        if result == 1:
            player1+=1

        if result == 2:
            player2+=1

    return player1, player2 # returning no of wins for each player 


A="R"
B="P"
K = 7
print(rockPaperScissors(A, B, K))