using namespace std;
#include<iostream>
#include"sort.cpp"
#include"size.cpp"
#include"resize.cpp"
// void sort (int * arr, int size){
//     int min_ind;
//     int min;
//     int new_ele;
//     int temp;
//     for(int i = 0; i < size-1; i++){
//         min_ind = i;
//         min = arr[i];
//         for(int j = i+1; j < size; j++){

//             new_ele = arr[j];
//             if(new_ele < min){
//                 min_ind = j;
//                 min = new_ele;
//             }



//         }
//         temp = arr[i];
//         arr[i]=min;
//         arr[min_ind] = temp;





//     }



// }
pair<int ** , int> getRepeated(int * arr){

    int size_arr = size(arr);
    int ** all_repeated = new  int*[size_arr];
    int * repeated = new int[size_arr];
    int count = 0;
    int count_all = 0;
    int i;
    for(i =1; i< size_arr; i++){
        if(arr[i] == arr[i-1]){
            repeated[count]=i-1;
            count++;
            continue;
        }else {
            repeated[count]=i-1;
            resize(repeated, count);
            count = 0;
            all_repeated[count_all]=repeated;
            count_all++;


        }
        
    }
    pair<int **, int> pair1;
    pair1.first = all_repeated;
    pair1.second = count_all;
    return pair1;
};

bool candies(int ages[], int ages_size,int packs[], int packs_size){
    
    sort(ages,ages_size);
    sort(packs,packs_size);
    

    for(int i =1; i< ages_size; i++){
        while(ages[i-1] == ages[i]){

        }


    }


    return true;
}

int main(){ 
    

    int arr [] ={5,-4,3,0,10,15};
    int size = sizeof(arr)/sizeof(arr[0]);
    sort(arr, size);
    for(int i =0; i < size; i++)
        printf("%d ", arr[i]);
    printf("\n");
    
    int *new_arr = new int[3];  
    new_arr = resize(arr, 3);
    int size_new = sizeof(new_arr)/sizeof(new_arr[0]);
    printf("%d",size_new);



    return 0;
}