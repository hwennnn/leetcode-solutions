class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        
        highestindex, h1, h2 = 0, -1, -1
        
        for i,num in enumerate(nums):
            if num > h1:
                h2 = h1
                h1 = num
                highestindex = i
                
            elif num > h2 and num < h1:
                h2 = num
                
        return highestindex if h1 >= h2*2 else -1