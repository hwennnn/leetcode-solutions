class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos, neg = [], []
        
        for x in nums:
            if x < 0:
                neg.append(x)
            else:
                pos.append(x)
        
        res = []
        
        for x, y in zip(pos, neg):
            res.append(x)
            res.append(y)
        
        return res