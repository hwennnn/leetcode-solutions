class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = Counter()
        i = maxCount = res = 0
        
        for j, x in enumerate(s):
            counter[x] += 1
            maxCount = max(maxCount, counter[x])
            
            while j - i + 1 - maxCount > k:
                counter[s[i]] -= 1
                i += 1
            
            res = max(res, j - i + 1)
        
        return res