class Solution:
    def minSwaps(self, s: str) -> int:
        count = res = 0
        
        for c in s:
            if c == '[':
                count += 1
            else:
                count -= 1
            
            if count < 0:
                count += 2
                res += 1
        
        return res