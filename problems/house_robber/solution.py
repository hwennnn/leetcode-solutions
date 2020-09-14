class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if_rob = 0
        if_not_rob = 0
        
        for num in nums:
            temp = if_rob
            if_rob = num + if_not_rob
            if_not_rob = max(temp, if_not_rob)
        
        return max(if_rob, if_not_rob)