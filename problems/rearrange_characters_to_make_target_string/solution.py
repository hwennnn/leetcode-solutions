class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        tc = Counter(target)
        sc = Counter(s)
        
        return min(sc[t] // tc[t] for t in tc)