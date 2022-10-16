class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        n = len(light)
        blues = [False] * n
        ons = [False] * n
        res = 0
        on = 0
        for i, x in enumerate(light):
            ons[x-1] = True
            # if idx == 0, then light it up to blue
            if x == 1 or blues[x-2]: 
                blues[x-1] = True

            r = x
            if blues[x-1]:
                while r < n and ons[r]:
                    blues[r] = True
                    on -= 1
                    r += 1
            else:
                on += 1
            
            if on == 0:
                res += 1
            
        return res
            