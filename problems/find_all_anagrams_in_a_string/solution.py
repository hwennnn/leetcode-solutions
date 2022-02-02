class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        pn = len(p)
        
        counter = Counter(p)
        required = pn
        start = 0
        res = []
        
        for end, x in enumerate(s):
            if x in counter:
                if counter[x] > 0:
                    required -= 1
                
                counter[x] -= 1
            
            while required == 0:
                if s[start] in counter:
                    counter[s[start]] += 1
                    if counter[s[start]] > 0:
                        required += 1
                
                if end - start + 1 == pn:
                    res.append(start)
                
                start += 1
        
        return res