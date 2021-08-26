class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority, count = nums[0], 1
        
        for i,x in enumerate(nums[1:], 1):
            if count == 0:
                count += 1
                majority = x
            elif majority == x:
                count += 1
            else:
                count -= 1
        
        return majority