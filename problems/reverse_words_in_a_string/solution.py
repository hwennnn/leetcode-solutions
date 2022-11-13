class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        curr = ""

        for x in s + " ":
            if x == " ":
                if curr:
                    res.append(curr)
                    curr = ""
            else:
                curr += x

        return " ".join(res[::-1])