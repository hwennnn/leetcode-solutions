class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        queue = [0]
        seen = set(queue)
        
        while queue:
            p = queue.pop()
            for room in rooms[p]:
                if room not in seen:
                    seen.add(room)
                    queue.append(room)
                    

        return n == len(seen)