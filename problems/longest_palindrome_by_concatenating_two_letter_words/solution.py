class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = Counter()
        res = 0
        middle = 0
        
        for word in words:
            if word == word[::-1]:
                if count[word] > 0:
                    count[word] -= 1
                    res += 4
                    middle -= 1
                else:
                    middle += 1
                    count[word] += 1
            else:
                if count[word[::-1]] > 0:
                    count[word[::-1]] -= 1
                    res += 4
                else:
                    count[word] += 1
        
        if middle > 0:
            res += 2
        
        return res