class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        
        A.sort()
        
        odd_lst = [i for i in A if i%2!=0]
        
        even_lst = [i for i in A if i%2==0]
        
        temp = []
        
        
        for i in range(len(A)):
            count = len(temp)//2
            if i%2 == 0:
                temp.append(even_lst[count])
                
            else:
                temp.append(odd_lst[count])
                
        return temp