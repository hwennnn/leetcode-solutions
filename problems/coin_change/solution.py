class Solution:
    def coinChange(self, coins, amount):
        level = seen = {0}
        number = 0
        
        while level:
            if amount in level:
                return number
            
            level = {a+c for a in level for c in coins if a+c <= amount} - seen
            seen |= level
            number += 1
            
        return -1
        