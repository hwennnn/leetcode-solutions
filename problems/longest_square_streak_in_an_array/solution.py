class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort(reverse = 1)
        count = {}
        
        for x in nums:
            count[x] = count.get(x * x, 0) + 1
        
        res = max(count.values())
        
        return res if res >= 2 else -1
        