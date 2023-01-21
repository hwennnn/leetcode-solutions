class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if k == 0: return 0 if nums1 == nums2 else -1
        inc = dec = 0
        
        for a, b in zip(nums1, nums2):
            diff = abs(a - b)
            
            if diff % k != 0: return -1
            
            if a - b >= 0:
                dec += diff // k
            else:
                inc += diff // k
                
        return inc if inc == dec else -1
        