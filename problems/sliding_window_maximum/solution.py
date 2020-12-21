class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq = collections.deque()
        res = []
        
        for i,x in enumerate(nums):
            
            if deq and i - k >= deq[0]:
                deq.popleft()
            
            while deq and x > nums[deq[-1]]:
                deq.pop()
            
            deq.append(i)
            
            if i + 1 >= k:
                res.append(nums[deq[0]])
        
        return res