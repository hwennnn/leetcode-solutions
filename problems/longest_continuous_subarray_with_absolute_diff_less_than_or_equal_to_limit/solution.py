class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxd = deque()
        mind = deque()
        i = res = 0
        
        for j,num in enumerate(nums):
            while len(maxd) and num > maxd[-1]: maxd.pop()
            while len(mind) and num < mind[-1]: mind.pop()
                
            maxd.append(num)
            mind.append(num)
            
            if maxd[0] - mind[0] > limit:
                if maxd[0] == nums[i]: maxd.popleft()
                if mind[0] == nums[i]: mind.popleft()
                i += 1
            
            res = max(res, j - i + 1)
        return res