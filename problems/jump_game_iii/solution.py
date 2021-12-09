class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        initial = [start + arr[start], start - arr[start]]
        visited = set(initial)
        deq = deque(initial)
        n = len(arr)
        
        while deq:
            curr = deq.popleft()
            
            if not 0 <= curr < n: continue
                
            if arr[curr] == 0: return True
            
            for x in (curr + arr[curr], curr - arr[curr]):
                if 0 <= x < n and x not in visited:
                    deq.append(x)
                    visited.add(x)

        
        return False