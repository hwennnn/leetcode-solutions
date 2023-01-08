class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        cnt1 = [0] * 26
        cnt2 = [0] * 26
        
        for x in word1:
            cnt1[ord(x) - ord('a')] += 1
        
        for x in word2:
            cnt2[ord(x) - ord('a')] += 1
        
        def check(cnt1, cnt2):
            return sum(1 for x in cnt1 if x > 0) == sum(1 for x in cnt2 if x > 0)
        
        for a in range(26):
            for b in range(26):
                if cnt1[a] > 0 and cnt2[b] > 0:
                    # if a in word1 swap with b in word2
                    cnt1[a] -= 1
                    cnt1[b] += 1

                    cnt2[a] += 1
                    cnt2[b] -= 1

                    if check(cnt1, cnt2):
                        return True
                    
                    cnt1[a] += 1
                    cnt1[b] -= 1

                    cnt2[a] -= 1
                    cnt2[b] += 1
        
        return False