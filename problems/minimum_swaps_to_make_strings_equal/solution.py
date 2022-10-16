class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        counter1, counter2 = Counter(s1), Counter(s2)
        
        if (counter1["x"] + counter2["x"]) % 2 and (counter1["y"] + counter2["y"]) % 2: return -1
        
        mp1, mp2 = Counter(), Counter()
        
        res = 0
        
        for c1,c2 in zip(s1,s2):
            if c1 != c2:
                if mp1[c1] > 0 and mp2[c2] > 0:
                    mp1[c1] -= 1
                    mp2[c2] -= 1
                else:
                    mp1[c1] += 1
                    mp2[c2] += 1
                    res += 1
        
        return res