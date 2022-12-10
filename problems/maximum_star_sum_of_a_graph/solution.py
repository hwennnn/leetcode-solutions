class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        N = len(vals)
        res = -inf
        graph = defaultdict(list)
        
        for a, b in edges:
            if vals[a] > 0:
                graph[b].append(vals[a])
            
            if vals[b] > 0:
                graph[a].append(vals[b])
            
        for node in range(N):
            graph[node].sort(reverse = 1)
            curr = vals[node]
            take = 0
            
            for val in graph[node]:
                curr += val
                take += 1
                
                if take == k: break
                
            res = max(res, curr)
        
        return res