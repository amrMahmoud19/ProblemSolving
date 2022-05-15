# function for detecting if there is a bomb in cell
def contain_integer(arr):
# ascii values for digits from 1-9 are 49-57
    for i in range(len(arr)):
        
        char_ascii = ord(arr[i])
        if char_ascii >= 49 and char_ascii <=57:
            return char_ascii - 48, i
    return -1,-1



# function for counting all the people found in array
def count_person(arr):
# Ascii for character P is 80
    no_persons = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if ord(arr[i][j]) == 80:
                no_persons+=1
    return no_persons



# function for updating the no of killed people due the bomb in a cell
def kill_person(arr, no_killed):
    for i in range(len(arr)):
        if ord(arr[i]) == 80:
            no_killed+=1
    return no_killed



# main function for counting the no of survivors
def survivors(arr):

    no_killed = 0

    for i in range(len(arr)):
        
        bomb_radius, bomb_index = contain_integer(arr[i])                   # arr[i] is the cell containing the bomb 

        if bomb_radius != -1:                                               # if there is a bomb found in the current cell

            for j in range(bomb_radius):
                if j!=0:                                                    # counting the number of killed people in the other cells due to the bomb in the current cell
                    if i-j >= 0:                                            # checking if cell is within array bounds
                        no_killed =  kill_person(arr[i-j], no_killed)
                        
                    if i+j < len(arr):                                      # chechking if cell within array bounds
                        no_killed = kill_person(arr[i+j], no_killed)

                else:                                                       # counting the number of killed people in the current cell due to the bomb
                    if bomb_index-j >=0:
                        no_killed+=1
                    if bomb_index+j < len(arr[i]):
                        no_killed+=1

    return count_person(arr) - no_killed                                    # no of survivors is: the number of killed people + all the people found in the array



mat = ["P***","****","**2P","****", "****", "**PP"]
print(survivors(mat))

                   


