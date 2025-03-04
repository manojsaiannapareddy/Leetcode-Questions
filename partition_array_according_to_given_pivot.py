class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        greater = []
        count = []
        if len(nums) == 1:
            return nums

        for i in range(len(nums)):
            if nums[i] < pivot:
                less.append(nums[i])
            elif nums[i] == pivot:
                count.append(pivot)
            else:
                greater.append(nums[i])
 
        return less + count + greater


        
        

                