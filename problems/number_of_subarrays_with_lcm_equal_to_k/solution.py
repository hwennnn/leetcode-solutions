class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        N = len(nums)
        res = 0
        
        for i in range(N):
            l = nums[i]
            
            for j in range(i, N):
                l = lcm(l, nums[j])
                
                if l > k: break
                
                if l == k:
                    res += 1
        
        return res
                
        
        