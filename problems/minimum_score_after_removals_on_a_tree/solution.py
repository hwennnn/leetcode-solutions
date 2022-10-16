class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        N, M = len(nums), len(edges)
        
        graph = defaultdict(list)
        children = defaultdict(set)
        xor = nums.copy()
        V = 0
        degree = [0] * N
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            degree[a] += 1
            degree[b] += 1
        
        seen = set()
        dq = deque()
        
        for node in range(N):
            V ^= nums[node]
            if degree[node] == 1:
                dq.append(node)
                seen.add(node)
        
        while dq:
            node = dq.popleft()
            
            for nei in graph[node]:
                if nei not in seen:
                    children[nei].add(node)
                    children[nei] |= children[node]
                    xor[nei] ^= xor[node]
                
                degree[nei] -= 1
                
                if degree[nei] == 1:
                    dq.append(nei)
                    seen.add(nei)
        
        res = float('inf')
        
        for i in range(M - 1):
            for j in range(i + 1, M):
                a, b = edges[i]
                
                if b in children[a]:
                    a, b = b, a
                
                c, d = edges[j]
                
                if d in children[c]:
                    c, d = d, c
                
                if a in children[c]:
                    curr = [xor[a], xor[c] ^ xor[a], V ^ xor[c]]
                elif c in children[a]:
                    curr = [xor[c], xor[a] ^ xor[c], V ^ xor[a]]
                else:
                    curr = [xor[c], xor[a], V ^ xor[c] ^ xor[a]]
                
                res = min(res, max(curr) - min(curr))
        
        return res