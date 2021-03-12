class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        _set = set()
        
        for i in range(n-k+1):
            _set.add(s[i:i+k])
        
        return len(_set) == 1 << k