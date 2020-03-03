class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        one = two = three = -float('inf')
        
        for i in nums:
            if i > one:
                one, two, three = i, one, two
            
            elif i > two and i < one:
                two, three = i, two
                
            elif i > three and i < two:
                three = i
                
        return three if three != -float('inf') else one