class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        graph = collections.defaultdict(list)
        
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        queue = collections.deque([(0, 0)])
        seen = set([0])
        res = float('-inf')
        
        while queue:
            x, distance = queue.popleft()
            
            if x != 0:
                d = distance * 2
                lastSent = (d - 1) // patience[x] * patience[x]
                res = max(res, d + lastSent)
            
            for y in graph[x]:
                if y not in seen:
                    seen.add(y)
                    queue.append((y, distance + 1))
        
        return res + 1
        