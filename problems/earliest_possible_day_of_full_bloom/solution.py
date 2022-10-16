class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        A = sorted(zip(plantTime, growTime), key = lambda x:-x[1])
        
        days = res = 0
        
        for plant, grow in A:
            days += plant
            
            res = max(res, days + grow)
        
        return res