class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        rows = len(grid)
        cols = len(grid[0]) 

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    temp = 4  
                    
                    if i > 0 and grid[i-1][j] == 1: 
                        temp -= 1
                    if i < rows - 1 and grid[i+1][j] == 1: 
                        temp -= 1
                    if j > 0 and grid[i][j-1] == 1: 
                        temp -= 1
                    if j < cols - 1 and grid[i][j+1] == 1:
                        temp -= 1
                    
                    ans += temp  

        return ans