class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        mp = collections.defaultdict(int)
        n = len(A)
        res = 0
        M = 10 ** 9 + 7
        
        for i in range(n):
            res = (res + mp[target - A[i]]) % M
            
            for j in range(i):
                t = A[i] + A[j]
                mp[t] += 1
        
        return res % M