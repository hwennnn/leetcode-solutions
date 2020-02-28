class Solution:
    def removeDuplicates(self, A: List[int]) -> int:
        
        if not A:
            return 0
        else:
            ii,jj=1,1
            while jj<len(A):
                if A[ii-1]!=A[jj]:
                    A[ii]=A[jj]
                    ii+=1
                jj+=1
                
            return ii