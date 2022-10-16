class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        
        for i,x in enumerate(nums):
            left = prefix[i]
            right = prefix[-1] - prefix[i+1]

            ans = (x*i - left) + (-x*(n-i-1) + right)
            res.append(ans)
        
        return res