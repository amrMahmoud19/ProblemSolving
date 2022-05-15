def subArray(arr):
    best_sum = 0                                                            #holds maximum sum value
    local_sum = 0                                                           #holds sum of current subarray
    max_left = 0                                                            #holds start index of current max value subarray
    max_right = 0                                                           # holds ending index of current max value subarray
    current_left = 0                                                        #holds start index of current subarray

    for i in range (0,len(arr)):
        #in case there is a negative value in subarray skip this element and start the new subarray from following element
        if(arr[i]<0):
            current_left = i+1                                                #changing current subarray start index to be after the negative element
            local_sum = 0                                                     #re-initilizing the sum of new subarray
            continue
        else:
           local_sum =  local_sum + arr[i]                                    #calculating sum of current subarray
           if(local_sum > best_sum):
               max_right = i                                                  #extending the ending index of subarray to include the current index of main array
               max_left = current_left                                        
               best_sum = local_sum                                           #updating the maximum sum value
    return arr[max_left:max_right+1], best_sum

arr = [1,2,5,1,5]
new_arr = subArray(arr)
print(new_arr)
