class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        stops = defaultdict(list)
        
        for i, route in enumerate(routes):
            for x in route:
                stops[x].append(i)
        
        dq = deque([(source, 0)])
        seen = set([source])
        
        while dq:
            o, steps = dq.popleft()
            
            if o == target: return steps
            
            for nxtStop in stops[o]:
                for stop in routes[nxtStop]:
                    if stop not in seen:
                        dq.append((stop, steps + 1))
                        seen.add(stop)
                
                routes[nxtStop] = []
        
        return -1