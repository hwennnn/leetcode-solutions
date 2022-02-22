class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = set()
        queue = deque([(x, 1) for x in range(1, 10)])
        
        while queue:
            x, length = queue.popleft()
            
            if length == n:
                res.add(x)
                continue
            
            last = x % 10
            
            if last + k < 10:
                queue.append((x * 10 + last + k, length + 1))
            
            if last - k >= 0:
                queue.append((x * 10 + last - k, length + 1))
        
        return list(res)