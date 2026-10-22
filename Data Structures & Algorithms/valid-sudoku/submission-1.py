class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sub_box_ = {i : set() for i in range(9)}
        row_ = {i : set() for i in range(9)}
        col_ = {i : set() for i in range(9)}

        for i in range(9):
            row = board[i]
            for j in range(9):
                cell = row[j]
                if cell == '.':
                    continue
                if cell in sub_box_[3*(i//3) + j//3]:
                    print(i,j,cell, sub_box_)
                    return False
                else :
                    sub_box_[3*(i//3) + j//3].add(cell)
                if cell in row_[i]:
                    print(i,j,cell, row_)
                    return False
                else :
                    row_[i].add(cell)
                if cell in col_[j]:
                    print(i,j,cell, col_)
                    return False
                else :
                    col_[j].add(cell)
        return True