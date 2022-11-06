class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        N = len(nums)
        i = 0
        curr = set()
        currSum = 0
        res = 0
        
        for j, x in enumerate(nums):
            while j - i + 1 > k or x in curr:
                curr.remove(nums[i])
                currSum -= nums[i]
                i += 1
            
            curr.add(x)
            currSum += x
            if j - i + 1 == k:
                res = max(res, currSum)
        
        return res