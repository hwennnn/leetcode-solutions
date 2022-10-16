class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        
        def non_coprime(x, y):
            return gcd(x, y) > 1
    
        def lcm(x, y):
            lcm = (x*y) // gcd(x,y)
            return lcm
        
        stack = []
        for x in nums:
            stack.append(x)
            
            while len(stack) >= 2 and non_coprime(stack[-1], stack[-2]):
                stack.append(lcm(stack.pop(), stack.pop()))

        return stack
                    