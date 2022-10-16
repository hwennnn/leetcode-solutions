class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        
        for x, y in dislikes:
            graph[x].append(y)
            graph[y].append(x)
        
        p = {}
        
        @cache
        def go(node):
            for hate in graph[node]:
                if hate in p:
                    if p[hate] == p[node]:
                        return False
                else:
                    p[hate] = -p[node]
                    if not go(hate):
                        return False
            
            return True
        
        for node in range(n):
             if node not in p:
                p[node] = 1
                if not go(node):
                    return False
        
        return True