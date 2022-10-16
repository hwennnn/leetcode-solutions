class Solution:
    def areSentencesSimilar(self, s1: str, s2: str) -> bool:
        s1 = s1.split()
        s2 = s2.split()
        
        def good(a, b):
            a = collections.deque(a)
            b = collections.deque(b)
            
            while len(a) > 0 and len(b) > 0 and a[0] == b[0]:
                a.popleft()
                b.popleft()
            
            while len(a) > 0 and len(b) > 0 and a[-1] == b[-1]:
                a.pop()
                b.pop()
            
            return len(a) == 0
        
        return good(s1, s2) or good(s2, s1)