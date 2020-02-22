class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        
        return [i for i in A if i%2==0] + [i for i in A if i%2==1]