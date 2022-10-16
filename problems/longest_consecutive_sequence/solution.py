class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        
        while s:
            first = last = s.pop()
            
            while first - 1 in s:
                s.remove(first - 1)
                first -= 1
            
            while last + 1 in s:
                s.remove(last + 1)
                last += 1
            
            res = max(res, last - first + 1)
        
        return res