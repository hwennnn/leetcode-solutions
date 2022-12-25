class Solution:
    def captureForts(self, forts: List[int]) -> int:
        N = len(forts)
        
        def go(A):
            curr = -1
            res = 0

            for x in A:
                if x == 1:
                    curr = 0
                elif x == 0:
                    curr += curr >= 0
                else:
                    res = max(res, curr)
                    curr = -1
            
            return res
        
        return max(go(forts), go(forts[::-1]))
