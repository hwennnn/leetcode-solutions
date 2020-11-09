class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        c = Counter(arr)
        v = sorted(c.values(), reverse = True)
        
        n = len(arr)
        half = n // 2
        res = 0
        
        for x in v:
            n -= x
            res += 1
            
            if n <= half:
                return res
        
        return res
        
        