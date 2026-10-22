DIRECTIONS = [(1,0), (0,1)]

class Solution:

    def getPathsFromPos(self, x:int, y:int, m:int, n:int):
        if (x==m) and (y==n):
            return 1
        if (x>m) or (y>n):
            return 0
        else :
            return self.getPathsFromPos(x+1, y, m, n) + self.getPathsFromPos(x, y+1, m, n)

    def uniquePaths(self, m: int, n: int) -> int:
        return self.getPathsFromPos(1, 1, m, n)
        