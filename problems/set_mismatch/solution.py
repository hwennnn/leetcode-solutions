class Solution:
    def findErrorNums(self, nums: List[int]):
        n = len(nums)
        mp = collections.Counter(nums)
        
        twice = zero = None
        
        for i in range(1,n+1):
            if mp[i] == 0: zero = i
            elif mp[i] == 2: twice = i
        
        return [twice,zero]
        