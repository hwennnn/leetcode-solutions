class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        res = []
        n = len(s)
        queue = deque([x for x in range(n + 1)])
        
        for x in s:
            if x == "I":
                res.append(queue.popleft())
            else:
                res.append(queue.pop())
        
        res.append(queue.pop())
        
        return res