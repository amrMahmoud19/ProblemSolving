using namespace std;
#include<iostream>
int grid [3][4] = { { 4, 3, 8, 4 }, { 9, 5, 1, 9 }, { 2, 7, 6, 2 } } ;
int rows = sizeof(grid)/sizeof(grid[0]);
int columns = sizeof(grid[0])/sizeof(grid[0][0]);


int magicSquare(){
    if (rows < 3 || columns < 3)
        return -1;
    int count = 0;
    int row_itr = rows - 3 + 1;
    int column_itr = columns - 3 +1;
    int sum_row[3];
    int sum_col[3];
    int sum_dig1[2];
    int sum_dig2[2];
    bool isMagic = true;
    for(int i = 0; i < row_itr; i++){

        for(int j = 0; j < column_itr ; j ++){

            for(int x = 0; x<3; x++){
                
                sum_row[x] = grid[i+x][j]+grid[i+x][j+1]+grid[i+x][j+2];
                sum_col[x] = grid[i][j+x]+grid[i+1][j+x]+grid[i+2][j+x];
                if(x!=0 && (sum_row[x]!=sum_row[x-1] || sum_col[x]!=sum_col[x-1]) ){
                    isMagic = false;
                    break;

                }
                    

                
            }
            if (!isMagic)
                continue;
            
        count++;
        }




    }




    return count;
}


int main(){


    cout << magicSquare();

    return 0;
}