class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
            
        n = len(nums)
        M = 10 ** 9 + 7
        res = 0

        for i in range(1, n-1):
            mid = bisect_left(prefix, 2 * prefix[i])
            right = bisect_right(prefix, (prefix[-1] + prefix[i]) // 2)
            res += max(0, min(n,right) - max(i+1, mid))
        
        return res % M