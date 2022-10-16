class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        c = collections.Counter(nums)
        c = sorted(c.items(), key = lambda x : (x[1],-x[0]))

        res = []
        
        for key,value in c:
            for _ in range(value):
                res.append(key)
        
        return res