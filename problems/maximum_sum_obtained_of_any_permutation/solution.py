class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:

        counts = [0] * (len(nums)+1)
        
        for r in requests:
            counts[r[0]] += 1
            counts[r[1]+1] -= 1
        
        for i in range(1, len(counts)):
            counts[i] += counts[i-1]
        
        counts = sorted(counts[:-1], reverse=True)
        nums = sorted(nums, reverse=True)
        
        res = 0
        for c,n in zip(counts, nums):
            res += c * n
        
        return res%(1000000000 + 7)
        
        
        