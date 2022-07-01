class Solution:
    def minWindow(self, s: str, t: str) -> str:
        k = len(t)
        counter = Counter(t)
        i = 0
        res = (100001, 0)
        
        for j, x in enumerate(s):
            if counter[x] > 0:
                k -= 1
                
            counter[x] -= 1
            
            while k == 0:
                if j - i + 1 < res[0]:
                    res = (j - i + 1, i)
                    
                if counter[s[i]] == 0:
                    k += 1
                    
                counter[s[i]] += 1
                i += 1
        
        return "" if res[0] == 100001 else s[res[1] : res[0] + res[1]]