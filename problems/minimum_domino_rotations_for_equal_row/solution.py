class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        a = collections.Counter(A)
        b = collections.Counter(B)
        mp = collections.defaultdict(int)
        
        for x,y in zip(A,B):
            if x == y:
                mp[x] += 1
                
        res = float("inf")
        for x in a:
            if (a[x] + b[x] - mp[x]) == n:
                res = min(res, min(a[x], b[x]) - mp[x])
    
        return res if res != float("inf") else -1
            
            