using namespace std;
#include<iostream>
// momken ainsert kolo fe ay 7eta b3den asort fe el akher
void printArr(int * arr, int size){


    for(int i =0; i< size; i++)
        cout << arr[i] << " ";

}
void insert(int * arr, int element,int index, int size){

    for(int i = size; i > index; i--){
        arr[i] = arr[i-1];

    }
    arr[index] = element;

    // printArr(arr, size);

    
}



int calcAbs(int * arr, int size){
    int sum = 0;
    for(int i =0; i < size-1; i++){
        sum+= (arr[i+1]-arr[i]);

    }

return sum;

}
int * minAbs(int x, int * arr, int size){
    int temp;
    int size_new = size + x;
    int * arr2 = new int[size_new];
    
    // generating array represeting sequence x
    for(int i = 1; i<=x;i++)
        arr2[i-1] = i;
    // printArr(arr2,size_new);
    // insert elements of arr sorted
    for(int j =0; j<size;j++){

        for(int k = 0; k<x; k++){
            if(arr[j] > arr2[k])
                continue;
            else{
               
               insert(arr2, arr[j],k,x+j);
                
                break;

            }
                

        }
        if(arr[j] > x)
            insert(arr2, arr[j],x+j ,x+j);
           

    }

    


    // printArr(arr2, size_new);
    return arr2;
}



int main(){

    int x = 8;
    int arr [] = {7,2,10};
    int size = sizeof(arr)/sizeof(arr[0]);
    int * new_arr = new int[size+x];
    new_arr = minAbs(8,arr,size);

    int sum = calcAbs(new_arr, size+x);

    printArr(new_arr, size+x);
    // for(int i =0; i< size+x; i++){
    //     cout << new_arr[i] + " ";
    // }
    cout << "\n";
    cout << "The minimum score is:"<<sum;



    return 0;
}