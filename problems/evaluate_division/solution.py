class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        cal = {}
        eq = defaultdict(dict)
        
        for (a, b), v in zip(equations, values):
            eq[a][b] = v
            eq[b][a] = 1.0 / v
        
        res = []
        
        def go(a, b):
            if a not in eq and b not in eq:
                return -1.0
                
            queue = deque([(a, 1.0)])
            visited = set()
            
            while queue:
                node, curr = queue.popleft()
                visited.add(node)
                
                for nei, val in eq[node].items():
                    if nei == b:
                        return curr * val
                    if nei in visited:
                        continue
                    
                    queue.append((nei, val * curr))
            
            return -1.0
        
        for a, b in queries:
            res.append(go(a, b))
        
        return res
            
            