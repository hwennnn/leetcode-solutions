class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        counter = Counter()
        have = False
        
        for x in nums:
            if x % 2 == 0:
                counter[x] += 1
                have = True
        
        if not have: return -1
        
        mmax = max(counter.values())
        
        for x in sorted(counter.keys()):
            if counter[x] == mmax:
                return x
        
        return -1