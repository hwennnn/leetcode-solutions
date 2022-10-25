class Solution:
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        N = len(nums)
        graph = defaultdict(list)
        total = sum(nums)
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def good(divisor):
            if total % divisor != 0: return False
            
            target = total // divisor
            count = 0
            visited = [False] * N
            
            def dfs(node):
                nonlocal count
                
                if visited[node]: return 0    
                visited[node] = True
                
                curr = nums[node]
                
                for nei in graph[node]:
                    curr += dfs(nei)
                
                if curr == target:
                    count += 1
                    curr = 0
                
                return curr
                
            dfs(0)
            return count == divisor
        
        for divisor in range(N, 0, -1):
            if good(divisor):
                return divisor - 1
        
        return 0