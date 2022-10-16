class Solution:
    def maxLengthBetweenEqualCharacters(self, S: str) -> int:
        
        d = collections.defaultdict(list)
        
        for i, s in enumerate(S):
            d[s].append(i)

        return max(d[i][-1] - d[i][0] - 1 for i in d)