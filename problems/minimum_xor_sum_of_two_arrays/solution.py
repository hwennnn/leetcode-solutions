class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums2)
        
        @cache
        def go(mask):
            i = bin(mask).count('1')
            if i >= len(nums1): return 0
            
            count = float('inf')
            
            for j in range(n):
                if mask & (1 << j) == 0:
                    count = min(count, (nums1[i] ^ nums2[j]) + go(mask + (1 << j)))
            
            return count
        
        return go(0)