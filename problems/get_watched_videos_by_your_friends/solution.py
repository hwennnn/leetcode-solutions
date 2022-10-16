class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], uid: int, level: int) -> List[str]:
        
        visited = {uid}
        deq = collections.deque([(uid, 0)])
        res = set()
        
        while deq:
            node, l = deq.popleft()
            
            if l > level: break
            
            if l == level: res.add(node)
            
            for nei in friends[node]:
                if nei not in visited:
                    deq.append((nei, l + 1))
                    visited.add(nei)
            
        videos = Counter([v for i in res for v in watchedVideos[i]])
        
        return sorted(videos, key = lambda x: (videos[x], x))
                