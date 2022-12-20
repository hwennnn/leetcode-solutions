class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        N = len(rooms)
        vis = [False] * N
        vis[0] = True

        def go(node):
            for nei in rooms[node]:
                if not vis[nei]:
                    vis[nei] = True
                    go(nei)
                    
        go(0)
        return all(vis)