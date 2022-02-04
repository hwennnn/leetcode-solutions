class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        res = count = 0
        table = {0 : -1}
        
        for i, x in enumerate(nums):
            if x == 0:
                count -= 1
            else:
                count += 1
            
            if count in table:
                res = max(res, i - table[count])
            else:
                table[count] = i
        
        return res