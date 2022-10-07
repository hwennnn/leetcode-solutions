class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        
        for x, y in tickets:
            graph[x].append(y)
        
        for x in graph:
            graph[x].sort(reverse = 1)

        S = "JFK"
        
        stack = [S]
        routes = []
        
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            routes.append(stack.pop())
        
        return routes[::-1]