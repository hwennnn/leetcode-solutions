class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        people.sort()
        res = 0
        i, j = 0, n - 1
        
        while i <= j:
            if i != j and people[i] + people[j] <= limit:
                res += 1
                i += 1
                j -= 1
            else:
                res += 1
                j -= 1
        
        return res