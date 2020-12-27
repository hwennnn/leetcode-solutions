class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = {start}
        deq = collections.deque([start])
        
        while deq:
            pos = deq.popleft()
            num = arr[pos]
            if arr[pos] == 0: return True
            
            for p in (pos + num, pos - num):
                if 0 <= p < len(arr) and p not in visited:
                    deq.append(p)
                    visited.add(p)
            
        
        return False
                    
        