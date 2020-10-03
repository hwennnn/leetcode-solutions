class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        ans = [[]]
        
        for i in range(n):
            tmp = []
            for num in ans:
                c = num + [nums[i]]
                tmp.append(c)
            
            ans += tmp
        
        return ans
                
        