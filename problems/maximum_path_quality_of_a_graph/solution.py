class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        res = float('-inf')
        graph = collections.defaultdict(list)
        
        for start, end, t in edges:
            graph[start].append((end, t))
            graph[end].append((start, t))
        
        def go(current, path, timeLeft):
            if current == 0:
                nonlocal res
                v = sum(values[x] for x in path)
                res = max(res, v)
            
            for nei, t in graph[current]:
                if timeLeft >= t:
                    go(nei, path | {nei}, timeLeft - t)
                    
        go(0, {0}, maxTime)
        return res