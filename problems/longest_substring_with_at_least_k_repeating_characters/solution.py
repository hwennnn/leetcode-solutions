class Solution:
    def longestSubstring(self, st: str, k: int) -> int:
        
        res = 0
        stack = [st]
        
        while stack:
            s = stack.pop()
            for c in set(s):
                if s.count(c) < k:
                    stack.extend([ch for ch in s.split(c)])
                    break
            else:    
                res = max(res, len(s))
        
        return res
        