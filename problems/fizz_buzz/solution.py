class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        temp = []
        
        for i in range(1,n+1):
            
            if i%3 == 0 and i%5 == 0:
                temp.append("FizzBuzz")
            
            elif i%3 == 0:
                temp.append("Fizz")
                
            elif i%5 == 0:
                temp.append("Buzz")
                
            else:
                temp.append(str(i))
                
        
        return temp
                
            