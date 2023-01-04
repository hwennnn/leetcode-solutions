class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        res = 0
        counter = Counter(tasks)
        
        for v in counter.values():
            if v == 1: return -1

            if v % 3 == 0:
                res += v // 3
            else:
                res += v // 3 + 1
        
        return res