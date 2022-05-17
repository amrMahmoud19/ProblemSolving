import numpy as np

def solitaire( cells,i, j, no_ex = 0):

    #  terminating condtion 
    size = len(cells)
   
    if (cells[i][j] != -1 ):
        
        # if(j<=1 and i == len(cells[i-1])-1):
        #     sum = 0
        #     final_index = -1
        #     for x in range(len(cells[i-1])):
    
        #         sum+= solitaire(cells,i-1,x)
        #         if cells[i-1][x] == 1:
        #             final_index = x
        #             print(final_index)
        #     if(sum == 1):
                
        #         return final_index
        #     else:
                
        #         return cells[i][j]
        return cells[i][j]
    
            
            
                
        
    
   
    else:
        if no_ex >= 3:
            cells[i][j] = cells[i-1][j]
        lim = (i-1)//2
        if(solitaire(cells, i-1,j,no_ex) == 1):
            # cells[i][j] =  int(bool(solitaire(cells, i-1, j)) ^ bool(solitaire(cells,i-1,j+1)) ^ bool(solitaire(cells,i-1,j+2)))
            cells[i][j] = int(not(bool(solitaire(cells,i-1,j+1,no_ex) == 1 and solitaire(cells,i-1,j+2,no_ex) == 0 and j<size) or bool(solitaire(cells,i-1,j-1,no_ex) == 1 and solitaire(cells,i-1,j-2, no_ex) == 0 and j>3 )or bool((bool(solitaire(cells,i-1,j-1,no_ex)) ^ bool(solitaire(cells,i-1,j+1,no_ex)))and j!=2 and j!=size+1)))
        else:
            if j <=size+1-lim*2:
                # cells[i][j] = int((bool(solitaire(cells,i-1,j+1)) & bool(solitaire(cells,i-1,j+2))) | (bool(solitaire( cells,i-1,j-1)) & bool(solitaire( cells,i-1, j-2))))
                cells[i][j] = int((solitaire(cells,i-1,j-1,no_ex)==1 and solitaire(cells,i-1,j-2,no_ex) == 1) or (solitaire(cells,i-1,j+1,no_ex)==1 and solitaire(cells,i-1,j+2,no_ex)==1))
            else:
                cells[i][j] = cells[i-1][j]
        if(bool(cells[i][j]) ^ bool(cells[i-1][j])):
            no_ex+=1
                

    

    if (j > 1):
        cells[i][j-1] = solitaire( cells,i, j-1,no_ex)
    
    return cells[i][j]


def intialize( arr):
    size = len(arr)
    cells = np.zeros((size,size+4), np.int8)
    
    for i in range (len(cells)):
        cells[i][0] = 0
        cells[i][1] = 0
        cells[i][len(cells[i])-1] = 0
        cells[i][len(cells[i])-2] = 0
    
        for j in range(2,len(cells[i])-2):
            cells[i][j] = -1
            if(i==0):
                cells[i][j] = arr[j-2]
        
    solitaire(cells,  size-1, len(cells[0]) -3)
    
    final_peg = -1
    for i in range(len(cells[size-1])):
        if cells[size-1][i]==1:
            final_peg = i-2
    return cells,final_peg
    
# sys.setrecursionlimit(4000)
# if __name__=='__main__':
arr = np.array([1,1,1,1,1,1,0,1], np.int32)

# cells = np.zeros((len(arr),len(arr)+2), np.int32)
    
# for i in range (len(cells)):
#     cells[i][0] = 0
#     cells[i][len(cells)-1] = 0

#     for j in range(1,len(cells[i])-1):
#         cells[i][j] = -1
#         if(i==0):
#             cells[i][j] = arr[j-1]
# print(cells)

last_shape, final_peg_location = intialize( arr)
print(last_shape, final_peg_location)
