class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        res = float('inf')
        graph = collections.defaultdict(list)
        
        for x, y in clips:
            graph[x].append(y)
        
        if len(graph[0]) == 0: return -1
        
        @cache
        def go(t, count):
            nonlocal res
            
            if t == time:
                res = min(res, count)
                return
            
            for nei in graph[t]:
                for x in range(t + 1, nei + 1):
                    go(x, count + 1)
            
        go(0, 0)
        
        return -1 if res == float('inf') else res