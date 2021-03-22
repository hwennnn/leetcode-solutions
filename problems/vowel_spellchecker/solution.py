class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        s1 = set(wordlist)
        s2 = set()
        mp = {}
        
        def mapped(word):
            return "".join(['_' if w in "aeiouAEIOU" else w.lower() for w in word])
        
        for i, w in enumerate(wordlist):
            l = "".join([c.lower() for c in w])
            s2.add(l)
            
            if l not in mp:
                mp[l] = i
                
            m = mapped(w)
            if m not in mp:
                mp[m] = i

        res = []
        for q in queries:
            l = "".join([c.lower() for c in q])
            h = mapped(q)
            if q in s1:
                res.append(q)
            elif l in s2:
                res.append(wordlist[mp[l]])
            elif h in mp:
                res.append(wordlist[mp[h]])
            else:
                res.append("")
        
        return res