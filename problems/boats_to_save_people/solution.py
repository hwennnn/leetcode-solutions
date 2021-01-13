class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        if n == 1: return 1
        
        people.sort(reverse = 1)
        i, j = 0, n-1
        boat = 0
        
        while i <= j:
            if i != j and people[i] + people[j] <= limit:
                i += 1
                j -= 1
                boat += 1
            else:
                i += 1
                boat += 1

        return boat
        