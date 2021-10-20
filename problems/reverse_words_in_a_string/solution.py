class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        curr = ""
        
        for c in s + " ":
            if c == " ":
                if curr:
                    res.append(curr)
                curr = ""
            else:
                curr += c
        
        return " ".join(res[::-1])