class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
            
        for i in range((len(str(x))//2)):
            if str(x)[i] != str(x)[((-1)-i)]:
                return False
            
        return True