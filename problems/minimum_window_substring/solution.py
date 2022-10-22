class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sn, tn = len(s), len(t)
        targetCounter = Counter(t)
        targetLength = len(targetCounter)
        res = (inf, -1)
        i = 0
        
        for j, x in enumerate(s):
            if x in targetCounter:
                targetCounter[x] -= 1
                if targetCounter[x] == 0:
                    targetLength -= 1
            
            while targetLength == 0:
                currSize = j - i + 1
                if currSize < res[0]:
                    res = (currSize, i)
                    
                if s[i] in targetCounter:
                    targetCounter[s[i]] += 1
                    if targetCounter[s[i]] == 1:
                        targetLength += 1
                
                i += 1

        return "" if res[0] == inf else s[res[1]: res[0] + res[1]]