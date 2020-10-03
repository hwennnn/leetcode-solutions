class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        nums.sort()
        ans = [[]]
        start = 1
        
        for i in range(n):
            tmp = []
            for j, num in enumerate(ans):
                if i > 0 and nums[i] == nums[i-1] and j < start: continue
                    
                c = num + [nums[i]]
                tmp.append(c)
            
            start = len(ans)
            ans += tmp
        
        return ans
                
        