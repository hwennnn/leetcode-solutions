class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        pos = -1
        
        for i in range(len(nums)):
            if nums[i] == 1:
                if pos != -1 and i - pos - 1 < k:
                    return False
                pos = i
        return True