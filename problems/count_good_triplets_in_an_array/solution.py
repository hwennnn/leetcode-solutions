from sortedcontainers import SortedList

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        pos = {x:i for i,x in enumerate(nums2)}
        
        sl = SortedList([pos[nums1[0]]])
        prefix = [0]
        
        for i in range(1, n):
            sl.add(pos[nums1[i]])
            prefix.append(sl.bisect_left(pos[nums1[i]]))
        
        sl = SortedList([pos[nums1[-1]]])
        suffix = [0]
        
        for i in range(n - 2, -1, -1):
            index = sl.bisect_left(pos[nums1[i]])
            suffix.append(len(sl) - index)
            sl.add(pos[nums1[i]])
        suffix.reverse()
        
        res = 0
        for a, b in zip(prefix, suffix):
            res += a * b
        
        return res
        