class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def go(node, prev):
            val = 2 if hasApple[node] else 0

            for nei in graph[node]:
                if prev != nei:
                    val += go(nei, node)

            return 2 + val if not hasApple[node] and val > 0 else val

        return max(0, go(0, -1) - 2)