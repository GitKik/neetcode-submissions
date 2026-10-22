OPERATIONS = [[1,0], [-1,0], [0,1], [0,-1]]



class Solution:
    def __init__(self):
        self.M = 0
        self.N = 0
        self.ids_to_check = set()
    def dig_island(self, grid: List[List[str]], x:int, y:int) -> set[int,int] :
        """
        get all the 
        """
        if (x<0) or (x>self.M-1) or (y<0) or (y>self.N-1) or ((x,y) not in self.ids_to_check):
            return 
        self.ids_to_check.discard((x,y))
        if grid[x][y] == "0" :
            return 
        else : 
            for op in OPERATIONS :
                op_x, op_y = op
                self.dig_island(grid,x + op_x, y + op_y)
            return 
        

    def numIslands(self, grid: List[List[str]]) -> int:
        self.M = len(grid)
        self.N = len(grid[0])
        for i in range(self.M):
            for j in range(self.N) :
                self.ids_to_check.add((i,j))
        # set of ids to go through 
        island_count = 0
        while self.ids_to_check :
            x,y = next(iter(self.ids_to_check))
            if grid[x][y] == "0":
                self.ids_to_check.discard((x,y))
            else : 
                island_count += 1 
                self.dig_island(grid, x, y)
        return island_count