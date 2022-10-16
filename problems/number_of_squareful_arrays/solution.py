class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        res = 0
        used = [False] * n
        
        @cache
        def good(m):
            sq = int(math.sqrt(m))
            
            return sq * sq == m
        
        def perm(path):
            nonlocal res
            
            if len(path) == n:
                res += 1
                return
            
            for i in range(n):
                if used[i]: continue
                    
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]: continue
                
                if len(path) == 0 or (len(path) > 0 and good(path[-1] + nums[i])):
                    used[i] = True
                    perm(path + [nums[i]])
                    used[i] = False
                
        perm([])        

        return res