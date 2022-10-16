class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        d = {"a":"bc", "b":"ac", "c":"ab"}
        q = collections.deque(["a","b","c"])
        
        while len(q[0]) < n:
            v = q.popleft()
            
            for u in d[v[-1]]:
                q.append(v+u)
        
        return q[k-1] if len(q) >= k else ""