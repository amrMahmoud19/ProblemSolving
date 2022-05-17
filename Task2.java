

int solitaire( int cells[][], int i, int j ) {

    // terminating condtion 
    if (cells[i][j] != -1 ){
        int sum = 0;
        for (int x = 0; i< cells[i-1].length(), x++){

            sum+= solitaire(cells,i-1,x);
            int final_index = cells[i-1][x] == 1 ? x: -1;

        }

        if(sum == 1)
            return final_index;
    }

    else{


        if(solitaire(cells,i-1,j) == 1)
            cells[i][j] = solitaire(cells, i-1, j) ^ solitaire(cells,i-1,j-1) ^ solotaire(cells,i-1,j+1);
        else 
            cells[i][j] = (solitaire(cells,i,j+1) ^ solitaire(cells,i-1,j+1)) | (solitaire(cells, i,j-1) ^ solitaire(cells, i-1, j-1));

        

    }



    return cells[i][j];
}