class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        column_hash = {i: set() for i in range(9)}
        sub_box_hash = {i: set() for i in range(9)}

        for i in range(len(board[0])):
            row_hash = set()
            for j in range(len(board)):
                if(board[i][j].isdigit()):
                    if(board[i][j] in row_hash):
                        return False
                    if(board[i][j] in column_hash[j]):
                        return False 
                    
                    sub_box = (i // 3) * 3 + (j // 3)
                    if(board[i][j] in sub_box_hash[sub_box]):
                        return False

                    sub_box_hash[sub_box].add(board[i][j])
                    column_hash[j].add(board[i][j])
                    row_hash.add(board[i][j])
        
        return True
                
