class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        
        def kadane(A):
            curr = res = 0
            
            for x in A:
                curr = max(curr + x, x)
                res = max(res, curr)
            
            return res
        
        def f(A, B):
            return sum(A) + kadane([b - a for a, b in zip(A, B)])
        
        return max(f(nums1, nums2), f(nums2, nums1))