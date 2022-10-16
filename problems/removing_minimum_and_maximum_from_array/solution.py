class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        mmax, mmin = float('-inf'), float('inf')
        maxi = mini = -1
        
        for i, x in enumerate(nums):
            if x > mmax:
                mmax, maxi = x, i
                
            if x < mmin:
                mmin, mini = x, i
            
        removeFromLeft = max(mini, maxi) + 1
        removeFromRight = n - min(mini, maxi)
        removeFromLeftAndRight = (min(mini, maxi) + 1) + (n - max(mini, maxi))
        
        return min(removeFromLeft, removeFromRight, removeFromLeftAndRight)