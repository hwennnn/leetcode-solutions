class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)

        xor = 0
        if n2 % 2 != 0:
            for x in nums1:
                xor ^= x
        
        if n1 % 2 != 0:
            for x in nums2:
                xor ^= x
        
        return xor