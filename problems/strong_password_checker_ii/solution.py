class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        n = len(password)
        if n < 8: return False
        
        lower = upper = numbers = special = 0
        
        for index, x in enumerate(password):
            if index + 1 < n and x == password[index + 1]:
                return False
        
            if x in string.ascii_letters:
                if x.islower():
                    lower += 1
                else:
                    upper += 1
            elif x.isdigit():
                numbers += 1
            else:
                special += 1

        return lower > 0 and upper > 0 and numbers > 0 and special > 0