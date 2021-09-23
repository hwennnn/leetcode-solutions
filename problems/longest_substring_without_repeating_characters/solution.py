class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sset = set()
        n = len(s)
        i = res = 0
        
        for j in range(n):
            while s[j] in sset:
                sset.remove(s[i])
                i += 1
            
            sset.add(s[j])

            res = max(res, len(sset))
        
        return res
                    