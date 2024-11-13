class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            ans = ""
            ans += s[i+1:] + s[0: i +1]
            if ans == goal:
                return True
        
        return False
        