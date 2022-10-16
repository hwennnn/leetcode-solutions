class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        people = [0] * 2051
        
        for b,d in logs:
            people[b] += 1
            people[d] -= 1

        for i in range(1, 2051):
            people[i] += people[i - 1]
            
        res = 0
        mmax = float('-inf')
        for i,x in enumerate(people):
            if x > mmax:
                res = i
                mmax = x
        
        return res