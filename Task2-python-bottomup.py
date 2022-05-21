# after running the script using cmd please enter the required array size (n) in the terminal
#  and then the output will be displayed in the terminal


import numpy as np

def solitaire(arr):

    size = len(arr)
    # initilizing the array containing all the moves
    # we padded the cells with two zeros on the left and two zeros on the right to avoid errors in moves that check on cells[i-1][j(+-)2]
    # that's why the shape is (size, size+4)
    cells = np.zeros((size,size+4), np.int8)
    sum_arr = 0
    for i in range(size):
        sum_arr+=arr[i]

    if sum_arr != size-1 :
        return -1

    if size <= 2:
        return -1
    if size%2 != 0:
        return -1
    if size > 4:
        if arr[size-2]!=0 and arr[size-5] != 0:
            return -1

    # initialize the padded cells on the right and left with zeros
    # initialize the cells under study with -1 except first row which contains initial array shape
    for x in range (len(cells)):
        cells[x][0] = 0
        cells[x][1] = 0
        cells[x][len(cells[x])-1] = 0
        cells[x][len(cells[x])-2] = 0
    
        for y in range(2,len(cells[x])-2):
            cells[x][y] = -1
            if(x==0):
                cells[x][y] = arr[y-2]
    # looping on each row to set its cells based on the moves done in the previous iteration
    for i in range(1,len(cells)):
        no_ex = 0                               # variable added to count the no of exchanges
                                                # so that no more than 3 exchanges are allowed per step/stage
                                                # as only one peg is moved per iteration/satge which causes 3 changes
                                                #  in cell values compared to cell values preceeding it
        
        lim = (i-1)//2                          # variable to check if we reached the point where
                                                #  the problem changed to problem of smaller input array
        

       
        # looping when the problem turns into a smaller problem (eg if input array was of size 10, after two steps
        #  it becomes now similar to the problem of an array of size 8), so we set the extra 2 cells with
        #  the same value as the cells in stage before it which always is zero
        for z in range(size+1, size+1-lim*2,-1):
            cells[i][z]=cells[i-1][z]

        for j in range(size+1-lim*2,1,-1):

            # in case 3 exchanges were done copy the rest of cell values from corresponding cell values in stage before it
            if no_ex >= 3:
                cells[i][j] = cells[i-1][j]
                continue
            # logic for changing one into zero in case it is a jumping peg cell or a jumped over cell
            if cells[i-1][j] == 1:
                # cells[i][j] =  int(bool(cells[i-1][j]) ^ bool(cells[i-1][j-1]) ^ bool(cells[i-1][j+1]))
                cells[i][j] = int(not(bool(cells[i-1][j+1] == 1 and cells[i-1][j+2] == 0 and j<size) or bool(cells[i-1][j-1] == 1 and cells[i-1][j-2] == 0 and j>3 )or bool((bool(cells[i-1][j-1]) ^ bool(cells[i-1][j+1]))and j!=2 and j!=size+1)))
            # logic for changing zero into one in case it is an empty cell that a peg will jump into to occupy 
            else:
                # cells[i][j] = int((bool(cells[i-1][j-1]) & bool(cells[i-1][j-2])) | (bool(cells[i-1][j+1]) & bool(cells[i-1] [j+2])))
                cells[i][j] = int((cells[i-1][j-1]==1 and cells[i-1][j-2] == 1) or (cells[i-1][j+1]==1 and cells[i-1][j+2]==1))
            # checking if an exchange
            if(bool(cells[i][j]) ^ bool(cells[i-1][j])):
                    no_ex+=1
    # terminating condition and returning the final peg location
    # in case we reached a row with only on cell filled i.e. only one elemnt in the row with one
    sum=0
    final_index = -1
    for z in range(2,len(cells[size-1])-2):
        sum+=cells[size-1][z]
        if cells[size-1][z] == 1:
            final_index = z
    
    # we return the index of the final peg location not its position in the input array 
    if sum == 1:
        print("Output Array is: " )
        print(cells[size-1][2:size+2])
        print("All output steps: ")
        print(cells)
        return final_index-2

    # print("Output Array is: " )
    # print(cells[size-1][2:size+2])
    else:
        return -1


# calling our function and printing the resulting final peg location

n = int(input())
# arr = np.array([1,1,1,1,1,0,1,1,1,1], np.int8)

for i in range(n):
    arr = [1]*n
    arr[i] = 0
    print("The input array is: ")
    print(arr)
    final_index= solitaire( arr)
    if(final_index == -1):
        print("invalid starting state")
    else:
        print("The single Remaning Peg index is: ")
        print(final_index)

