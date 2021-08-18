class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        memo = {}
        
        def backtrack(i):
            if i in memo: return memo[i]
            
            if i == n: return 1
            
            curr = 0
            
            # single char
            if s[i] != "0" and i < n:
                curr += backtrack(i + 1)
            
            # two char
            if s[i] != "0" and i + 1 < n and int(s[i : i + 2]) <= 26:
                curr += backtrack(i + 2)
            
            memo[i] = curr
            
            return curr
            
        return backtrack(0)
                