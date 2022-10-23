class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        
        def parse(event):
            hours, minutes = map(int, event.split(":"))
            
            return hours * 60 + minutes
        
        s1, e1 = map(parse, event1)
        s2, e2 = map(parse, event2)
        
        return s1 <= s2 <= e1 or s2 <= s1 <= e2