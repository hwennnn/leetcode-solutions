class Solution:
    def checkString(self, s: str) -> bool:
        aCount = 0
        a = s.count("a")
        
        for c in s:
            if c == "a":
                aCount += 1
            elif c == "b":
                if aCount != a:
                    return False
        
        return True