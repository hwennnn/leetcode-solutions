class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = Counter()
        res = leftover = 0
        
        for word in words:
            if word[0] == word[1]:
                if count[word] > 0:
                    leftover -= 1
                    res += 4
                    count[word] -= 1
                else:
                    count[word] += 1
                    leftover += 1
            else:
                if count[word[::-1]] > 0:
                    res += 4
                    count[word[::-1]] -= 1
                else:
                    count[word] += 1
        
        if leftover > 0:
            res += 2
        
        return res