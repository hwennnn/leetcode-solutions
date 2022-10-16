class Solution:
    def getHint(self, S: str, G: str) -> str:
        s = {}
        g = {}
        c = b = 0
        
        for i in range(len(S)):
            if S[i] == G[i]:
                b += 1
            else:
                s[S[i]] = s.get(S[i],0) + 1
                g[G[i]] = g.get(G[i],0) + 1
        
        
        for i in s:
            if i in g:
                c += min(s[i], g[i])
                
        return '{0}A{1}B'.format(b, c)
