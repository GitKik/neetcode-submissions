class Solution:

    memo = []
    
    def getPathsFromPos(self, x:int, y:int, m:int, n:int):
        if (x==m-1) and (y==n-1):
            return 1
        if (x>=m) or (y>=n):
            return 0
        if self.memo[x][y] != -1 :
            return self.memo[x][y]
        else :
            self.memo[x][y] = self.getPathsFromPos(x+1, y, m, n) + self.getPathsFromPos(x, y+1, m, n)
            return self.memo[x][y]
    def uniquePaths(self, m: int, n: int) -> int:
        self.memo = [[-1] * n for _ in range(m)]

        return self.getPathsFromPos(0, 0, m, n)
        