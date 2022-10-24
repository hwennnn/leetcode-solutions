class Solution:
    def compress(self, chars: List[str]) -> int:
        N = len(chars)
        prev = chars[0]
        count = 1
        index = 0
        
        for i in range(1, N + 1):
            if i < N and chars[i] == prev:
                count += 1
            else:
                chars[index] = prev
                index += 1
                
                if count != 1:
                    for x in str(count):
                        chars[index] = x
                        index += 1
                
                if i < N:
                    prev, count = chars[i], 1

        return index