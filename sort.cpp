using namespace std;
void sort (int * arr,int size){
    int min_ind;
    int min;
    int new_ele;
    int temp;
    for(int i = 0; i < size-1; i++){
        min_ind = i;
        min = arr[i];
        for(int j = i+1; j < size; j++){

            new_ele = arr[j];
            if(new_ele < min){
                min_ind = j;
                min = new_ele;
            }



        }
        temp = arr[i];
        arr[i]=min;
        arr[min_ind] = temp;





    }



}