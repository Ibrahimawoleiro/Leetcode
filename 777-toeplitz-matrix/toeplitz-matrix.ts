function isToeplitzMatrix(matrix: number[][]): boolean {
    let checker: boolean = false;
    for(let row_index = 0; row_index < matrix.length; row_index++){
        for (let col_index = 0; col_index < matrix[0].length; col_index++){
            if(row_index == 0){
                break;
            }
            if(col_index == 0){
                continue;
            }
            if (matrix[row_index - 1][col_index - 1] != matrix[row_index][col_index]){
                return checker;
            }
        }
    }
    return !checker;
};