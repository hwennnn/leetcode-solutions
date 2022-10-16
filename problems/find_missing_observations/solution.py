class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        mn = n + m
        curr = sum(rolls)
        total = mean * mn
        required = total - curr
        
        if required < n or 6 * n < required: return []
        
        count, mod = divmod(required, n)
        res = [count] * n
        
        for i in range(mod):
            res[i] += 1
        
        return res