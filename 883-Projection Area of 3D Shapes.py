class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        for i in range(len(grid)):
            ans += max(grid[i])
            temp = 0
            for j in range(len(grid[i])):
                if grid[i][j] >0:
                    ans += 1
                if grid[j][i] > temp:
                    temp = 0 + grid[j][i]
            ans += temp
        return ans