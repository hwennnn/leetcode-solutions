class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        deq = collections.deque()
        
        for i in range(len(nums)):
            nums[i] += (0 if not deq else nums[deq[0]])
            
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()
            
            if nums[i] > 0:
                deq.append(i)
            
            if i >= k and deq and deq[0] == i - k:
                deq.popleft()

        
        return max(nums)