class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        queue = collections.deque()
        pn = len(part)
        
        def check():
            i = -1
            for _ in range(pn):
                if queue[i] != part[i]: return False
                i -= 1
            
            return True
        
        for x in s:
            queue.append(x)
            
            while len(queue) >= pn and check():
                for _ in range(pn):
                    queue.pop()
            
        return "".join(queue)