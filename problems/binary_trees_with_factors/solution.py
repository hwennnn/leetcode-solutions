class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        n = len(arr)
        A = set(arr)
        M = 10 ** 9 + 7
        res = 0
        
        @cache
        def go(parent):
            cnt = 1
            
            for x in arr:
                if parent % x != 0: continue
                
                t = parent // x
                
                if t in A:
                    cnt += go(x) * go(t)
                    cnt %= M
            
            return cnt % M
        
        for x in arr:
            res += go(x)
            res %= M
        
        return res % M