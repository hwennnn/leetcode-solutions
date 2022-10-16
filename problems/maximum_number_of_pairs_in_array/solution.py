class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        n = len(nums)
        removed = 0
        
        for x in Counter(nums).values():
            removed += x // 2
        
        return [removed, n - removed * 2]