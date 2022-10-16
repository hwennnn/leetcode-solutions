class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        
        @cache
        def dp(i, mask):
            if i == n: return 0
            
            res = float('inf')
            
            for j in range(n):
                if mask & (1 << j) > 0:
                    res = min(res, dp(i + 1, mask ^ (1 << j)) + (nums1[i] ^ nums2[j]))
                
            return res
        
        return dp(0, (1 << n) - 1)