class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        
        def helper(left, right):
            count = 0
            
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1
            
            return count
        
        for mid in range(n):
            res += helper(mid, mid)
            res += helper(mid, mid + 1)
        
        return res