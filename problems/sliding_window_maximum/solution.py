class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = []
        queue = collections.deque()
        
        for i,x in enumerate(nums):
            while queue and x >= nums[queue[-1]]:
                queue.pop()
            
            queue.append(i)
            
            if i + 1 >= k:
                res.append(nums[queue[0]])
                
            if queue and i + 1 - k >= queue[0]:
                queue.popleft()
        
        return res