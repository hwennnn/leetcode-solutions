class Solution:
    def makeFancyString(self, s: str) -> str:
        deque = collections.deque()
        
        for c in s:
            deque.append(c)
            
            while len(deque) >= 3 and deque[-1] == deque[-2] == deque[-3]:
                deque.pop()
        
        return "".join(deque)