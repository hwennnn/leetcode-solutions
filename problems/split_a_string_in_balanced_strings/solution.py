class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        r_count = l_count = total = 0
        for i in s:
            l_count += (i=="L")
            r_count += (i=="R")
            total += (l_count==r_count)
            
        return total