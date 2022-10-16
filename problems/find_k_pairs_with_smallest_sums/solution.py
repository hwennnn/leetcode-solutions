class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n1, n2 = len(nums1), len(nums2)
        pq = []
        res = []
        
        for i in range(min(n1, k)):
            heappush(pq, ((nums1[i] + nums2[0]), i, 0))
            
        for _ in range(k):
            if not pq: break
                
            _, i, j = heappop(pq)
            res.append([nums1[i], nums2[j]])
            if j == n2 - 1: continue
            heappush(pq, (nums1[i] + nums2[j + 1], i, j + 1))

        return res