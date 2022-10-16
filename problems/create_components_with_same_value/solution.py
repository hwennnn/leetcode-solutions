class Solution:
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        N = len(nums)
        graph = defaultdict(list)
        total = sum(nums)
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def good(k):
            if total % k != 0: return False
            
            target = total // k
            visited = [False] * N
            count = 0
            
            def go(node):
                nonlocal count
                
                if visited[node]: return 0
                visited[node] = True
                
                currSum = nums[node]
                for nei in graph[node]:
                    currSum += go(nei)
                
                if currSum == target:
                    count += 1
                    return 0
                
                return currSum 
            
            go(0)

            return count == k
        
        for i in range(N, 0, -1):
            if good(i):
                return i - 1
        
        return 0