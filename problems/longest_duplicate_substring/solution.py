class Solution:
    def robinKarp(self, s, M):
        if M == 0: return 0
        
        q = (1 << 31) - 1
        h = pow(256, M - 1, q)
        d = 256
        t = 0
        mp = collections.defaultdict(list)
        
        for i in range(M):
            t = (t * d + ord(s[i])) % q
        mp[t].append(0)
        
        for i in range(len(s) - M):
            t = (d * (t - ord(s[i]) * h) + ord(s[i + M])) % q
            
            for j in mp[t]:
                if s[j : j + M] == s[i + 1 : i + 1 + M]:
                    return (True, s[j : j + M])
            mp[t].append(i + 1)
        
        return (False, '')
        
    def longestDupSubstring(self, s: str) -> str:
        left, right = 0, len(s)
        res = ''
        
        while left + 1 < right:
            mid = left + (right - left) // 2
            isFound, word = self.robinKarp(s, mid)
            
            if isFound:
                left, res = mid, word
            else:
                right = mid
            
        return res
        