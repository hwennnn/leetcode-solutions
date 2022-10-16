class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        res = 0
        mp = Counter()
        n = len(nums)
        
        for i in range(n):
            for j in range(i+1, n):
                product = nums[i] * nums[j]
                
                res += mp[product]
                
                mp[product] += 1
            
        
        return res * 8