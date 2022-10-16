class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        M = 10 ** 9 + 7
        m, n = len(words[0]), len(target)
        count = defaultdict(lambda: defaultdict(int))
        
        for word in words:
            for i, x in enumerate(word):
                count[x][i] += 1
        
        @cache
        def go(i, k):
            if i == n:
                return 1
            
            if k == m:
                return 0
            
            res = go(i, k + 1)
            
            if count[target[i]][k] > 0:
                res += go(i + 1, k + 1) * count[target[i]][k]
                res %= M
            
            return res
        
        return go(0, 0)
        
        