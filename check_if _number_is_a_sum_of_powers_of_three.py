class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            temp = n % 3
            if temp == 2:
                return False
            
            n = n//3
        
        return True
        