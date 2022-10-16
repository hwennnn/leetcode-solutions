class Solution:
    def equalSubstring(self, s: str, t: str, cost: int) -> int:
        i = 0
        
        for j, (a,b) in enumerate(zip(s, t)):
            cost -= abs(ord(a) - ord(b))
            
            if cost < 0:
                cost += abs(ord(s[i]) - ord(t[i]))
                i += 1
        
        return j - i + 1