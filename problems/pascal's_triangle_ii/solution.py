class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        ans = []
        prev = None
        
        for i in range(1,rowIndex+2):
            temp = []
            
            for j in range(1,i+1):
                if j == 1 or j == i:
                    temp.append(1)
                else:
                    temp.append(prev[j-1]+prev[j-2])
                    
            ans.append(temp)
            prev = temp
            
        
        return ans[rowIndex]
                