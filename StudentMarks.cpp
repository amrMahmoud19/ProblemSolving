using namespace std;
#include<iostream>
#include"sort.cpp"


pair<string, int> rank_std(string names [], int marks [], int updates [],int size){
    pair<string, int> pair1;
    int *new_marks = new int [size];
    int max = 0;
    int max_ind = -1;
    for(int i =0; i<size;i++){
        new_marks[i] = marks[i] + updates[i];
        if(new_marks[i]>=max){
            max = new_marks[i];
            max_ind = i;
        }
        
    }
    pair1.first = names[max_ind];
    pair1.second = max_ind;
    // sort(new_marks, size);
    return pair1;

}
int main(){
    string names [] = {"sam","ram","geek"};
    int marks [] = {80,79,75};
    int updates [] = {0, 1, -9};
    int size = sizeof(marks)/sizeof(marks[0]);
    pair<string, int> pair1;
    pair1 = rank_std(names, marks, updates, size);

    cout<< pair1.first+"\n";
    cout << pair1.second;
    
    return 0;
}