class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        num_set = set()
        ans = [0,0]

        for nums in grid:
            for num in nums:
                if num in num_set:
                    ans[0] = num
                num_set.add(num)
        
        ans[1] = (((len(grid)*len(grid[0]))*(len(grid)*len(grid[0]) + 1))//2) - sum(num_set)
        return ans