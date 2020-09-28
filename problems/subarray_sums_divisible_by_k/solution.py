class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        
        prefix = {0:1}
        c = res = 0
        
        for num in A:
            c += num
            if c%K in prefix:
                res += prefix[c%K]
            prefix[c%K] = prefix.get(c%K, 0) + 1
        
        return res