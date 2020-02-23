class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        length = 0

        for word in words:
            check = True

            char_lst = [i for i in chars]

            for char in word:
                if char in char_lst:
                    char_lst.remove(char)

                else:
                    check = False

            if check:
                length += len(word)
                
        return length