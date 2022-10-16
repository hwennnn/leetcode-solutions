class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums: return []
        
        maj1, maj2, count1, count2 = 0, -1, 0, 0
        
        for num in nums:
            if num == maj1:
                count1 += 1
            
            elif num == maj2:
                count2 += 1
            
            elif count1 == 0:
                maj1, count1 = num, 1
            
            elif count2 == 0:
                maj2, count2 = num, 1
            
            else:
                count1 -= 1
                count2 -= 1
        
        return [n for n in (maj1, maj2) if nums.count(n) > len(nums) // 3]