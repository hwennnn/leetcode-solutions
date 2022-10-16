class Solution:
    def minDeletions(self, s: str) -> int:
        count = Counter(s)
        res = 0
        seen = set()
        
        for v in count.values():
            while v > 0 and v in seen:
                res += 1
                v -= 1
            
            if v > 0:
                seen.add(v)
            
        return res
        