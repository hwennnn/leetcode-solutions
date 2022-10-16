class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        if n1 * 6 < n2 or n1 > n2 * 6: return -1
        
        sum1, sum2 = sum(nums1), sum(nums2)
        if sum1 > sum2: return self.minOperations(nums2, nums1)
        
        nums1.sort()
        nums2.sort()
        
        i, j ,res = 0, n2 - 1, 0
        
        while sum2 > sum1:
            if (j < 0 or i < n1) and 6 - nums1[i] > nums2[j] - 1:
                sum1 += 6 - nums1[i]
                i += 1
            else:
                sum2 -= nums2[j] - 1
                j -= 1
            
            res += 1
            
        return res