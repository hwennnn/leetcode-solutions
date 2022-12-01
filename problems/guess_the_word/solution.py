# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        def similarity(A, B):
            count = 0

            for a, b in zip(A, B):
                if a == b:
                    count += 1
            
            return count

        i = matches = 0

        while i < 10 and matches != 6:
            guess = words[randint(0, len(words) - 1)]
            temp = []

            matches = master.guess(guess)

            for word in words:
                if similarity(word, guess) == matches:
                    temp.append(word)

            words = temp
            i += 1