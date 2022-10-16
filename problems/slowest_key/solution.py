class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        mp = collections.defaultdict(int)
        curr = 0
        
        for time, key in zip(releaseTimes, keysPressed):
            t = time - curr
            mp[key] = max(mp[key], t)
            curr = time
        
        mp = list(mp.items())
        res = mp[0]
        
        for char, t in mp:
            if t > res[1] or (t == res[1] and char > res[0]):
                res = (char, t)
        
        return res[0]