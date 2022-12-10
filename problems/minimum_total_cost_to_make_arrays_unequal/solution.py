class Solution:
    def minimumTotalCost(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)
        counter = defaultdict(int)
        dominant = -1
        dominantFreq = 0
        res = 0
        swaps = 0

        for i, (a, b) in enumerate(zip(nums1, nums2)):
            if a == b:
                counter[a] += 1
                if counter[a] > dominantFreq:
                    dominantFreq = counter[a]
                    dominant = a
                res += i
                swaps += 1
        
        for i in range(N):
            if dominantFreq > swaps // 2 and nums1[i] != nums2[i] and nums1[i] != dominant and nums2[i] != dominant:
                swaps += 1
                res += i
        
        if dominantFreq > swaps // 2:
            return -1
        
        return res
