class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        res = 0
        
        mp = collections.defaultdict(int)
        
        for a in A:
            for b in B:
                mp[a+b] += 1
        
        for c in C:
            for d in D:
                res += mp[-(c+d)]
        
        return res
            