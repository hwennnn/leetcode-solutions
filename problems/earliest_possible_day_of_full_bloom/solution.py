class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        A = sorted([(plant, grow) for plant, grow in zip(plantTime, growTime)], key = lambda x:-x[1])
        res = 0
        days = 0
        
        for plant, grow in A:
            days += plant
            res = max(res, days + grow)
        
        return res