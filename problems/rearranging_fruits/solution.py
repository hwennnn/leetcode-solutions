class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        cnt = Counter()
        
        for x in basket1:
            cnt[x] += 1
        
        for x in basket2:
            cnt[x] -= 1
        
        mmin = min(basket1 + basket2)
        A = []
        
        for k, v in cnt.items():
            if v % 2 == 1: return -1
            
            A += [k] * abs(v // 2)
        
        A.sort()
        res = 0
        
        for i in range(len(A) // 2):
            res += min(mmin * 2, A[i])
        
        return res