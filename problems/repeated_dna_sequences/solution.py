class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        mp = {"A": 1, "C": 2, "G": 3, "T": 4}
        q = (1 << 31) - 1
        h = (pow(4, 9)) % q
        seen, res = set(), set()
        t = 0
        
        for i, x  in enumerate(s):
            if i >= 10:
                t -= (mp[s[i - 10]] * h)
            t = (4 * t + mp[x]) % q

            if i >= 9 and t in seen:
                res.add(s[i - 9: i + 1])
            else:
                seen.add(t)
        
        return list(res)
        
        