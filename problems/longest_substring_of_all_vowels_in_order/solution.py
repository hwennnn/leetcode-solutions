class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        if "a" not in word: return 0
        v = ["a", "e", "i", "o", "u"]

        vi = 0
        n = len(word)
        curr = res = 0
        i = j = word.index("a")
        while j < n and word[j] == "a":
            j += 1
        vi += 1

        while i < n and j < n:
            if word[j] != v[vi]:
                vi = 0
                i = j
                
                while j < n and word[j] != v[vi]:
                    j += 1
                i = j

            if j >= n: return res
            
            while j < n and word[j] == v[vi]:
                j += 1
            
            vi += 1
            if vi == 5: 
                res = max(res, j - i)
                vi = 0
                i = j
            
        return res