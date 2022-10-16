class Solution:
    def specialArray(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        for i in range(n+1):
            c = 0
            for num in nums:
                if num >= i:
                    c += 1
            if c == i:
                return i
        
        return -1