class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = collections.defaultdict(list)
        
        for x, y in relations:
            graph[y - 1].append(x - 1)
        
        @cache
        def go(x):
            res = 0
            
            for node in graph[x]:
                res = max(res, go(node))    
            
            return time[x] + res
        
        return max(go(i) for i in range(n))