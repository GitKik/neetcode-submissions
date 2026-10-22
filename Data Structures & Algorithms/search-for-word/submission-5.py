
DIRECTION = [(1,0), (-1,0), (0,1), (0,-1)]

class Solution :
    def checkWord(self,
                  index: Tuple[int, int],
                  used_index: List[tuple[int, int]],
                  board: List[List[str]], 
                  sub_string:str):
        if len(sub_string) == 0 :
            return [True]
        m, n = len(board), len(board[0])
        x, y = index[0], index[1]
        print((x,y))

        if board[x][y] == sub_string[0]:
            print(sub_string)
            if len(sub_string) == 1:
                return [True]
            used_index += [(x,y)]
            ret = []
            for direction in DIRECTION :
                x_n = x + direction[0]
                y_n = y + direction[1]
                usd_new = [u for u in used_index]
                if (x_n >= 0) and (y_n>=0) and (x_n<m) and (y_n<n) and ((x_n,y_n) not in used_index) :
                    ret += self.checkWord((x_n,y_n), usd_new, board, sub_string[1:])
            return ret

        else:
            return [False]

    def exist(self, board: List[List[str]], word: str) -> bool:
        ret = []
        ww = self.checkWord(index=(0,0), used_index=[], board=board, sub_string=word)
        print(ww)
        for i in range(len(board)) :
            for j in range(len(board[0])) :
                ww = self.checkWord(index=(i,j), used_index=[], board=board, sub_string=word)
                print(ww)
                if True in ww :
                    return True
        return False

        