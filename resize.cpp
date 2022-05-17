int * resize(int * arr,int new_size){

    int * new_arr = new int[new_size];
    for(int i =0; i< new_size; i++)
        new_arr[i]=arr[i];

    return new_arr;
    

}