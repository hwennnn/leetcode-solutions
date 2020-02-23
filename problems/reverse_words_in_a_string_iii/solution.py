class Solution:
    def reverseWords(self, s: str) -> str:
        
        temp = [i[::-1] for i in s.split(" ")]

        return " ".join(temp)