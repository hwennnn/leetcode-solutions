class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        idx = n-1
        i,j = 0, n-1
        
        while i <= j:
            if abs(nums[i]) > abs(nums[j]):
                res[idx] = nums[i] * nums[i]
                i += 1
            else:
                res[idx] = nums[j] * nums[j]
                j -= 1
            
            idx -= 1
        return res