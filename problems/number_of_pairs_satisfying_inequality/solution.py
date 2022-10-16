from sortedcontainers import SortedList

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        N = len(nums1)
        sl = SortedList()
        res = 0
        
        # nums1[i] - nums1[j] <= nums2[i] - nums2[j] + diff
        # nums1[i] - nums2[i] <= diff + nums1[j] - nums2[j]
        
        for j in range(N):
            curr = diff + nums1[j] - nums2[j]
            
            index = sl.bisect_right(curr)
            res += index
            
            sl.add(nums1[j] - nums2[j])
        
        return res