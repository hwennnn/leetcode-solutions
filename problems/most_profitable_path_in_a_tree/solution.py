class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        N = len(amount)
        parents = defaultdict(set)
        graph = defaultdict(list)
        level = {}
        
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        visited = [False] * N
        def dfs(node, parent, l):
            level[node] = l
            visited[node] = True
            if parent != -1:
                parents[node].add(parent)
            
            for nei in graph[node]:
                if not visited[nei]:
                    dfs(nei, node, l + 1)
        
        dfs(0, -1, 0)
        res = -inf
        A = [(0, amount[0])]
        vis = [False] * N
        vis[0] = True
        B = set([bob])
        al, bl = level[0], level[bob]
        unlocked = set([bob])

        while A:
            nxtA = []
            nxtB = set()
            
            for node in B:
                for parent in parents[node]:
                    if parent != -1 and level[parent] == bl - 1:
                        nxtB.add(parent)
            
            for node, income in A:
                if len(graph[node]) == len(parents[node]) and income > res:
                    res = income
                    
                for nei in graph[node]:
                    if not vis[nei]:
                        vis[nei] = True
                        amt = amount[nei]

                        if nei in nxtB:
                            nxtA.append((nei, income + amt // 2))
                        elif nei in unlocked:
                            nxtA.append((nei, income))
                        else:
                            nxtA.append((nei, income + amt))

            al += 1
            bl -= 1
            A = nxtA
            B = nxtB
            unlocked |= B
        
        return res
                         