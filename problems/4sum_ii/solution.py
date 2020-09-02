class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        AB = {}
        res = 0
        
        for a in A:
            for b in B:
                AB[a+b] = AB.get(a+b,0) + 1
        
        for c in C:
            for d in D:
                res += AB.get(-c-d,0)
        
        return res