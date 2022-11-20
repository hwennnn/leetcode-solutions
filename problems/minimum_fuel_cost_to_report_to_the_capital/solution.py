class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        N = len(roads)
        res = 0
        graph = defaultdict(list)

        for x, y in roads:
            graph[x].append(y)
            graph[y].append(x)
        
        def go(node, prev):
            nonlocal res

            people = 1

            for nei in graph[node]:
                if nei != prev:
                    people += go(nei, node)
            
            if node != 0:
                res += ceil(people / seats)
            
            return people

        go(0, 0)
        return res