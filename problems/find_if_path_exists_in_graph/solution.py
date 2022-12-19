class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        vis = [False] * n
        vis[source] = True
        st = [source]

        while st:
            node = st.pop()
            if node == destination: 
                return True

            for nei in graph[node]:
                if not vis[nei]:
                    st.append(nei)
                    vis[nei] = True
        
        return False