import numpy as np

def solitaire(arr):

    size = len(arr)
    
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
    if arr[size-2]!=0 and arr[size-5] != 0:
        return -1

    
    for x in range (len(cells)):
        cells[x][0] = 0
        cells[x][1] = 0
        cells[x][len(cells[x])-1] = 0
        cells[x][len(cells[x])-2] = 0
    
        for y in range(2,len(cells[x])-2):
            cells[x][y] = -1
            if(x==0):
                cells[x][y] = arr[y-2]
    
    for i in range(1,len(cells)):
        no_ex = 0                              
        lim = (i-1)//2                         
        

       
       
        for z in range(size+1, size+1-lim*2,-1):
            cells[i][z]=cells[i-1][z]

        for j in range(size+1-lim*2,1,-1):

            
            if no_ex >= 3:
                cells[i][j] = cells[i-1][j]
                continue
            
            if cells[i-1][j] == 1:
                
                cells[i][j] = int(not(bool(cells[i-1][j+1] == 1 and cells[i-1][j+2] == 0 and j<size) or bool(cells[i-1][j-1] == 1 and cells[i-1][j-2] == 0 and j>3 )or bool((bool(cells[i-1][j-1]) ^ bool(cells[i-1][j+1]))and j!=2 and j!=size+1)))
            
            else:
                
                cells[i][j] = int((cells[i-1][j-1]==1 and cells[i-1][j-2] == 1) or (cells[i-1][j+1]==1 and cells[i-1][j+2]==1))
            
            if(bool(cells[i][j]) ^ bool(cells[i-1][j])):
                    no_ex+=1
    
    sum=0
    final_index = -1
    for z in range(len(cells[size-1])):
        sum+=cells[size-1][z]
        if cells[size-1][z] == 1:
            final_index = z
    
    
    if sum == 1:
        print(cells[size-1][2:size+2])
        return final_index-2

    print(cells)
    return final_index-2



arr = np.array([1,1,1,1,0,1], np.int8)
final_index= solitaire( arr)
print(final_index)
