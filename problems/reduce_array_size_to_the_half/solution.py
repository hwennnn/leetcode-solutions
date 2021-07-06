class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        t = (n + 1) // 2
        count = collections.Counter(arr)
        res = 0
        
        for v in sorted(count.values(), reverse = 1):
            n -= v
            res += 1
            if n <= t: return res
        
        return res
        