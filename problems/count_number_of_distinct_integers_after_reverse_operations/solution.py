class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        res = set()
        
        for x in nums:
            res.add(x)
            
            r = int(str(x)[::-1])
            
            res.add(r)
        
        return len(res)