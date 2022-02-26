class Solution:
    def movesToStamp(self, S: str, T: str) -> List[int]:
        if S == T: return [0]
        
        S, T = list(S), list(T)
        sn, tn = len(S), len(T)
        res = []
        sDiff = tDiff = True
        
        while tDiff:
            tDiff = False
            
            for i in range(tn - sn + 1):
                sDiff = False
                for j in range(sn):
                    if T[i + j] == "*": continue
                    if T[i + j] != S[j]: break
                    sDiff = True
                else:
                    if sDiff:
                        for j in range(i, i + sn):
                            T[j] = "*"
                        tDiff = True    
                        res.append(i)
        
        return reversed(res) if all(c == "*" for c in T) else []