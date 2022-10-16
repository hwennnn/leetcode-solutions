class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        
        def isSubsequence(s, t):
            t = iter(t)
            
            return all(c in t for c in s)
        
        hot = "".join(key * (value // k) for key, value in Counter(s).items())
        combs = set()
        
        for i in range(len(hot) + 1):
            for comb in combinations(hot, i):
                for perm in permutations(comb):
                    combs.add("".join(perm))
        
        combs = sorted(combs, key = lambda x: (len(x), x), reverse = 1)
        
        for comb in combs:
            if isSubsequence(comb * k, s):
                return comb