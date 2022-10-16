class Solution:
    def minSwaps(self, s: str) -> int:
        ones = zeroes = 0
        
        for c in s:
            if c == '0':
                zeroes += 1
            else:
                ones += 1
        
        if abs(zeroes - ones) > 1: return -1
        
        def countSwap(char):
            count = 0
            for c in s:
                if c != char:
                    count += 1
                char = '1' if char == '0' else '0'
            
            return count // 2
        
        if zeroes > ones:
            return countSwap('0')
        elif ones > zeroes:
            return countSwap('1')
        else:
            return min(countSwap('0'), countSwap('1'))