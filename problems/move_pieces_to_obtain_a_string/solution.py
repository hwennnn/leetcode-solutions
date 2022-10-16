class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if start == target: return True
        
        s = [(i, x) for i, x in enumerate(start) if x != "_"]
        t = [(i, x) for i, x in enumerate(target) if x != "_"]
        
        if len(t) != len(s): return False
        
        for index, (a, b) in enumerate(zip(s, t)):
            i, x = a
            j, y = b
            
            if x != y: return False

            if x == "L":
                if i < j: return False
            else:
                if i > j: return False

        
        return True