class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        
        color = {}

        def go(node):
            for hate in graph[node]:
                if hate not in color:
                    color[hate] = -color[node]
                    if not go(hate):
                        return False
                else:
                    if color[hate] == color[node]:
                        return False
            
            return True

        for node in range(1, n + 1):
            if node not in color:
                color[node] = 1
                if not go(node):
                    return False
        
        return True
        
