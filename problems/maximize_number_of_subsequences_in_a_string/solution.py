class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        p1, p2 = pattern
        
        if p1 == p2:
            n = text.count(p1) + 1
            
            return n * (n - 1) // 2
        
        def count(s):
            res = curr = 0
            
            for x in s:
                if x == p1:
                    curr += 1
                elif x == p2:
                    res += curr
            
            return res
        
        return max(count(p1 + text), count(text + p2))