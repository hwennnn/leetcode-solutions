class Solution:
    def countTime(self, time: str) -> int:
        res = 0
        
        for hour in range(24):
            for minutes in range(60):
                x = f"{hour:02}:{minutes:02}"
                
                for a, b in zip(time, x):
                    if a != b and a != "?":
                        break
                else:
                    res += 1
        
        return res