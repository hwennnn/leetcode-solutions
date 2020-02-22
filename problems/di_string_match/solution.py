class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        
        low,high = 0,len(S)
        temp = []
        
        for i in S:
            
            if i == "I":
                temp.append(low)
                low+=1
                
            elif i == "D":
                temp.append(high)
                high-=1
                
                
        return temp + [low]