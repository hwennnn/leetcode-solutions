class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        pq = [(0, src, k + 1)]
        graph = defaultdict(list)
        seen = {}

        for a, b, price in flights:
            graph[a].append((b, price))

        while pq:
            weight, node, stops = heappop(pq)

            if node == dst: return weight
            
            if node in seen and seen[node] >= stops: continue

            seen[node] = stops

            if stops > 0:
                for adj, adjW in graph[node]:
                    heappush(pq, (weight + adjW, adj, stops - 1))

        return -1