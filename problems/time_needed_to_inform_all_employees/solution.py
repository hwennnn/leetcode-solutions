class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        
        for x, y in enumerate(manager):
            if y == -1: continue
                
            graph[y].append(x)
        
        @cache
        def go(node):
            res = 0
            
            for nei in graph[node]:
                res = max(res, go(nei) + informTime[node])
            
            return res
        
        return go(headID)