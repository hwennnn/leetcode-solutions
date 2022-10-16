class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        count = Counter(tasks).values()
        res = 0
        
        for x in count:
            if x == 1: return -1
            
            if x % 3 == 0:
                res += x // 3
            else:
                res += x // 3 + 1
        
        return res