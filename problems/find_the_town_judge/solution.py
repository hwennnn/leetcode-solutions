class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted = [0] * (n + 1)
        trust_other = [0] * (n + 1)
        
        for u, v in trust:
            trusted[v] += 1
            trust_other[u] += 1
        
        for i in range(1, n + 1):
            if trusted[i] == n - 1 and trust_other[i] == 0:
                return i
        
        return -1