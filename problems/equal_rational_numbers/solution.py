class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        
        def g(s):
            s2 = ""
            rep1 = ""
            ok = False

            for x in s:
                if x == "(" or x == ")":
                    ok = True
                    continue

                if ok:
                    rep1 += x
                else:
                    s2 += x
            
            return (s2, rep1)
        
        os1, rep1 = g(s)
        os2, rep2 = g(t)
        s1 = os1 + rep1 * 30
        s2 = os2 + rep2 * 30
        if len(rep1) == 0 and len(rep2) == 0:
            return s1 == s2 or float(s1) == float(s2)
        
        if s1 == s2 or float(s1) == float(s2): return True

        
        def good(s1, s2):
            count = 1
            curr = s1[-1]
            roundCount = len(s2) - 2
            
            for i in range(len(s1) - 2, -1, -1):
                if curr == s1[i]:
                    count += 1
                else:
                    return False
                
                if i > 0 and s1[i] != s1[i - 1] and count >= 30:
                    ss = s1[:i + 1]
                    r = float(ss) + float("0." + "0" * (len(ss) - 3 - bool(s1[i - 1] == ".")) + "1")
                    
                    if r == float(s2):
                        return True
            
            return False
        
        return good(s1, s2) or good(s2, s1)
        
            
        
        