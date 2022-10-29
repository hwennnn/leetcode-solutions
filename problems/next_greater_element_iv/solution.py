class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = [-1] * N
        stack = []
        pq = []
        
        for i, x in enumerate(nums):
            while pq and x > pq[0][0]:
                rx, ri = heappop(pq)
                res[ri] = x

            while stack and x > nums[stack[-1]]:
                popIndex = stack.pop()
                heappush(pq, (nums[popIndex], popIndex))
            
            stack.append(i)

        return res