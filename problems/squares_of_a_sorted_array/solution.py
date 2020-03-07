class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
    
        temp = [None] * n
        
        left, right = 0, n-1
        
        for i in reversed(range(n)):
            
            if abs(nums[left]) > abs(nums[right]):
                
                temp[i] = nums[left] ** 2
                left += 1
                
            else:
                
                temp[i] = nums[right] ** 2
                right -=1
                
        
        return temp
                