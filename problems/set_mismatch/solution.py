class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        N = len(nums)
        s = set()
        dup = -1
        total = N * (N + 1) // 2
        
        for x in nums:
            if x in s:
                dup = x
            else:
                s.add(x)
                total -= x
        
        return [dup, total]
        