class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = [0] * (n - k + 1)
        queue = collections.deque()
        
        for i in range(n):
            
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()
            
            queue.append(i)
            
            if i + 1 >= k:
                res[i - k + 1] = nums[queue[0]]
            
                if i - queue[0] >= k - 1:
                    queue.popleft()
        
        return res