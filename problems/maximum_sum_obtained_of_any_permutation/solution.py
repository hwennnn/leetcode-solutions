class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        M = 10 ** 9 + 7
        n = len(nums)
        p = [0] * (n+1)

        for s,e in requests:
            p[s] += 1
            p[e+1] -= 1
        
        for i in range(1, n+1):
            p[i] += p[i-1]
        
        nums.sort(reverse = True)
        p.sort(reverse = True)
        res = 0
        for i,x in enumerate(nums):
            res += x * p[i]
            res %= M
        
        return res