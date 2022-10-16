class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        
        def parse(nums):
            s = nums.split('+')
            
            return int(s[0]), int(s[1][:-1])
        
        n1, i1 = parse(num1)
        n2, i2 = parse(num2)
        
        n = n1 * n2 - i1 * i2
        i = n1 * i2 + n2 * i1
        
        return "{}+{}i".format(n, i)

            