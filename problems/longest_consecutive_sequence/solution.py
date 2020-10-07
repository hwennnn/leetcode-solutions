class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        
        while s:
            first = last = s.pop()
            
            while first - 1 in s:
                first -= 1
                s.remove(first)
            
            while last + 1 in s:
                last += 1
                s.remove(last)
            
            res = max(res, last - first + 1)
        
        return res