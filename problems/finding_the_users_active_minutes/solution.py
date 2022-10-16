class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        res = [0] * k
        mp = collections.defaultdict(set)
        
        for i, time in logs:
            mp[i].add(time)
        
        for v in mp.values():
            res[len(v) - 1] += 1
        
        return res