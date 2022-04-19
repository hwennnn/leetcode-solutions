class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        s = []
        
        for x in nums:
            index = bisect_left(s, x)
            
            if index >= len(s):
                s.append(x)
            else:
                s[index] = x
        
        return len(s)