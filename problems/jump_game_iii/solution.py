class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        queue = deque([start])
        visited = [False] * n
        visited[start] = True
        
        while queue:
            index = queue.popleft()
            
            if arr[index] == 0: return True
            
            for j in [(index + arr[index]), (index - arr[index])]:
                if 0 <= j < n and not visited[j]:
                    visited[j] = True
                    queue.append(j)
        
        return False