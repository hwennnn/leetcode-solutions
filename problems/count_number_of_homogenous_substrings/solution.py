class Solution:
    def countHomogenous(self, s: str) -> int:
        n = len(s)
        M = 10 ** 9 + 7
        res = 0
        
        mp = Counter(s)
        
        i = 0
        while i < n:
            j = i + 1
            while j < n and s[i] == s[j]:
                res += j - i
                j += 1
            
            i = j
        
        return (res + sum(mp.values())) % M