class Solution:
    def similarPairs(self, words: List[str]) -> int:
        N = len(words)
        res = 0
        
        for i in range(N):
            a = sorted(set(words[i]))
            for j in range(i + 1, N):
                b = sorted(set(words[j]))
                
                if a == b:
                    res += 1
                
        return res