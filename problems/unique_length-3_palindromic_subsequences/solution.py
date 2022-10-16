class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        n = len(s)
        mp = collections.defaultdict(list)
        
        for i,x in enumerate(s):
            mp[x].append(i)
        
        for key in mp:
            ll = mp[key]
            if len(ll) >= 2:
                ss = set(s[ll[0] + 1 : ll[-1]])     
                res += len(ss)

        return res
        