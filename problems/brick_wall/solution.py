class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        n = len(wall)
        
        mp = collections.defaultdict(int)
        
        for bricks in wall:
            start = 0
            for i in range(len(bricks) - 1):
                start += bricks[i]
                mp[start] += 1
        
        return n - (max(mp.values()) if len(mp) > 0 else 0)
            