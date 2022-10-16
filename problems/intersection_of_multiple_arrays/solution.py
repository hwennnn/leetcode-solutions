class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        count = Counter()
        
        for arr in nums:
            for x in arr:
                count[x] += 1
        
        res = []
        
        for k, v in count.items():
            if v == n:
                res.append(k)
        
        return sorted(res)