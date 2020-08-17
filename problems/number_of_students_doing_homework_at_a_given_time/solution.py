class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        
        count = 0
        
        for i,j in zip(startTime, endTime):
            count += queryTime<= j and queryTime >= i
            
        return count