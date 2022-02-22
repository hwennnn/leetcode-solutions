class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        wordList = set(wordlist)
        words = {}
        shuffled = {}
        done_shuffled = set()
        res = []
        
        
        for word in wordlist:
            lower = word.lower()
            
            if lower not in words:
                words[lower] = word
            
            if lower in done_shuffled: continue
                
            # word, current processed index
            queue = deque([(word.lower(), 0)])
            
            while queue:
                currWord, index = queue.popleft()
                
                if index == len(word): continue
                
                if currWord[index] in "aeiou":
                    for vowel in "aeiou":
                        newWord = currWord[:index] + vowel + currWord[index + 1:]
                        if newWord not in shuffled:
                            shuffled[newWord] = word
                        queue.append((newWord, index + 1))
                else:
                    queue.append((currWord, index + 1))
            
            done_shuffled.add(word)
            
        for word in queries:
            if word in wordList:
                res.append(word)
                continue
            
            lower = word.lower()
            
            if lower in words:
                res.append(words[lower])
                continue
            
            if lower in shuffled:
                res.append(shuffled[lower])
                continue
            
            res.append("")
        
        return res