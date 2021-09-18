class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = currStep = currFarthest = 0
        
        for i,x in enumerate(nums[:-1]):
            currFarthest = max(currFarthest, i + x)
            
            if i == currStep:
                jumps += 1
                currStep = currFarthest
        
        return jumps