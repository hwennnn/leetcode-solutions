class Solution:
    def intersect(self, A: List[int], B: List[int]) -> List[int]:
        dic = collections.Counter(A)
        res = []
        
    
        for num in B:
            if num in dic and dic[num] > 0:
                res += num,
                dic[num] -= 1
        
        return res