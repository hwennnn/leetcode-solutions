class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        
        deq = collections.deque()
        curr = 0
        
        for i in range(len(nums)-1, -1, -1):
            curr = nums[i] + (0 if not deq else nums[deq[0]])
            
            while deq and curr > nums[deq[-1]]:
                deq.pop()
            
            deq.append(i)
            
            if deq[0] >= i + k:
                deq.popleft()
            
            nums[i] = curr
        
        return curr