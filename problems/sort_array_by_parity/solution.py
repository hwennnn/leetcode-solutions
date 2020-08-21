class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        odd = []
        even = []
        
        for num in A:
            if num % 2:
                odd.append(num)
            else:
                even.append(num)
                
        return even+odd
                