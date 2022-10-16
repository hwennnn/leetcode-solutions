class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n = len(nums)
        m = (2 ** maximumBit) - 1
        res = []
        
        for i in range(1, n):
            nums[i] ^= nums[i - 1]

        for num in nums[::-1]:
            res.append(num ^ m)
            
        return res