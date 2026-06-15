class Solution {
    public boolean isValidSudoku(char[][] board) {
        Set<String> check = new HashSet<>();
        for(int i = 0 ; i < 9;i++){

            for(int j = 0 ;j<9;j++){
                
                char value = board[i][j];
                    if( value == '.'){
                        continue;
                    }
                String rowkey = "row" + i + value;
                String colkey = "col" + j + value;
                String boxkey = "box" +  (i/3)*3 + (j/3) + value;

                if( !check.add(rowkey) || !check.add(colkey)|| !check.add(boxkey)){
                    return false;
                }



            }
        }
        return true;
    }
}
