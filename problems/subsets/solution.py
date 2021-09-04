class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        
        for mask in range(1 << n):
            temp = []
            for j in range(n):
                if (mask >> j) & 1:
                    temp.append(nums[j])
            
            res.append(temp)
        
        return list(res)