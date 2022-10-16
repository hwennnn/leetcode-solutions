class Solution:
    def canFinish(self, n: int, A: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        visited = [0] * n
        
        for a, b in A:
            graph[b].append(a)
        
        def dfs(i):
            if visited[i] == -1:
                return False
            
            if visited[i] == 1:
                return True
            
            visited[i] = -1
            
            for j in graph[i]:
                if not dfs(j): 
                    return False
                
            visited[i] = 1
            
            return True
        
        for i in range(n):
            if not dfs(i): 
                return False
        
        return True