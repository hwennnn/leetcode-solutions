class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        mp = [0] * (N+2)
        
        for a,b in trust:
            mp[a] -= 1
            mp[b] += 1
        
        for i in range(1, N+1):
            if mp[i] == N - 1: return i
        
        return -1
            