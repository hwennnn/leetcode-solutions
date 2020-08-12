class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        prev = None
        
        for i in range(1,numRows+1):
            temp = []
            for j in range(1,i+1):
                
                if j == 1 or j == i:
                    temp.append(1)
                else:
                    temp.append(prev[j-1]+prev[j-2])
                    
            ans.append(temp)
            prev = temp

        return ans