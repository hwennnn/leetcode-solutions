class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = collections.defaultdict(list)
        
        for i, (x1, y1, r1) in enumerate(bombs):
            for j, (x2, y2, r2) in enumerate(bombs):
                if i == j: continue
                
                if (x1 - x2) ** 2 + (y1 - y2) ** 2 <= r1 * r1:
                    graph[i].append(j)
        
        def go(x):
            deque = collections.deque([x])
            seen = set([x])
            
            while deque:
                cand = deque.popleft()
                
                for nei in graph[cand]:
                    if nei not in seen:
                        deque.append(nei)
                        seen.add(nei)
            
            return len(seen)
        
        res = 0
        
        for i in range(n):
            res = max(res, go(i))
        
        return res