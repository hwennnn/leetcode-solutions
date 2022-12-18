class Solution:
    def isPossible(self, N: int, edges: List[List[int]]) -> bool:
        degree = [0] * N
        graph = [set() for _ in range(N)]
        
        for a, b in edges:
            a -= 1
            b -= 1
            degree[a] += 1
            degree[b] += 1
            graph[a].add(b)
            graph[b].add(a)
        
        odd_count = 0
        odds = []
        
        for i in range(N):
            if degree[i] % 2 == 1:
                odds.append(i)
                odd_count += 1
                
        if odd_count == 0: return True
        
        if odd_count == 2:
            a, b = odds
            
            if a not in graph[b]: return True
        
            for node in range(N):
                if node == a or node == b: continue
                
                if node not in graph[a] and node not in graph[b]:
                    return True
                
        elif odd_count == 4:
            for perm in permutations(odds, 4):
                a, b, c, d = list(perm)
                
                if a not in graph[b] and c not in graph[d]:
                    return True
        
        return False