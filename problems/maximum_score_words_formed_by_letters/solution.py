class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        N = len(words)
        res = 0
        counter = Counter(letters)

        for mask in range(1, 1 << N + 1):
            ok = True
            total = 0
            curr = Counter()

            for j in range(N):
                if mask & (1 << j) > 0:
                    for char in words[j]:
                        if curr[char] < counter[char]:
                            k = ord(char) - ord('a')
                            total += score[k]
                            curr[char] += 1
                        else:
                            ok = False
                            break


            if ok and total > res:
                res = total

        return res