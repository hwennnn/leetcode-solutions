class Solution:
    def toGoatLatin(self, S: str) -> str:
        
        vowel = ["a","e","i","o","u"]
        
        words = [i for i in S.split(" ")]

        count = 1
        lst= []
        for word in words:
            temp = ""
            if word[0].lower() in vowel:
                for char in word:
                    temp += char

                temp+="ma"

            else:
                l = word[0]
                for i in range(1,len(word)):
                    temp+=word[i]

                temp+=l
                temp+="ma"

            for _ in range(count):
                temp+="a"
            count+=1
            lst.append(temp)

        return " ".join(lst)