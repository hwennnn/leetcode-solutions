class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        mmin = curr = 0
        
        for x in nums:
            curr += x
            mmin = min(mmin, curr)
        
        return mmin if mmin > 0 else abs(mmin) + 1