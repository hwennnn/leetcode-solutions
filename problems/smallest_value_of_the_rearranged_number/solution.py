class Solution:
    def smallestNumber(self, num: int) -> int:
        if num >= 0:
            s = sorted(str(num))
            
            for i in range(len(s)):
                if s[i] > "0":
                    s[i], s[0] = s[0], s[i]
                    break
            
            return int("".join(s))
        else:
            num = -num
            s = sorted(str(num))
            
            return -int("".join(s[::-1]))
